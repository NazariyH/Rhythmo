<template>
    <div class="section">
        <form>
            <div id="paypal-button-container"></div>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Payment',
    data() {
        return {
            is_premium: false,
        }
    },
    mounted() {
        const token = localStorage.getItem('token')
        if (!token) {
            this.$router.push({ 'name': 'login' })
            return
        }

        this.checkUserSubscribement().then(() => {
            if (!this.is_premium) {
                this.loadPayPalSDK().then(() => {
                    this.renderPayPalButton()
                })
            }
        })
    },
    methods: {
        async checkUserSubscribement() {
            const token = localStorage.getItem('token')

            try {
                const response = await axios.get('payment-process/', {
                    headers: {
                        'Authorization': `Token ${token}`
                    }
                })

                this.is_premium = response.data.is_premium
            } catch (error) {
                console.log(error)
            }
        },


        async processSuccessfulPayment() {
            const token = localStorage.getItem('token')

            try {
                const response = await axios.post('payment-process/', null, {
                    headers: {
                        'Authorization': `Token ${token}`
                    }
                })

                this.$router.push({ 'name': 'current-profile' })
            } catch (error) {
                console.log(error)
            }
        },

        loadPayPalSDK() {
            return new Promise((resolve) => {
                if (window.paypal) {
                    resolve()
                    return;
                }
                const script = document.createElement('script')
                script.src = 'https://www.paypal.com/sdk/js?client-id=AUUCSiAkPHbLltngsUVuvJtDJrHxkw3lalioSeroVK-lQX5cs2JASpJ4dRCPoGso8V6yloxyCf0QJ6V6'
                script.onload = () => {
                    resolve();
                };
                document.body.appendChild(script)
            });
        },
        renderPayPalButton() {
            paypal.Buttons({
                style: {
                    color: 'black',
                    shape: 'rect',
                    label: 'subscribe',
                    height: 40
                },

                createOrder: (data, actions) => {
                    // Use PayPal's built-in order creation for testing
                    return actions.order.create({
                        purchase_units: [{
                            amount: {
                                value: '10.00' // Set a test amount
                            }
                        }]
                    }).then(orderID => {
                        return orderID // Return the order ID for further processing
                    })
                },
                onApprove: (data, actions) => {
                    // Capture the order for testing
                    this.processSuccessfulPayment()
                    return actions.order.capture().then(details => {
                        alert('Transaction completed by ' + details.payer.name.given_name)
                    });
                },
                onError: (err) => {
                    console.error('PayPal Checkout onError', err)
                    alert('An error occurred during the transaction. Please try again.')
                }
            }).render('#paypal-button-container')
        }
    }
}
</script>

<style scoped>
/* Add any styles specific to this component here */
</style>