<template>
    <div class="container">
        <form v-on:submit.prevent="signup">
            <div class="form-title input-block active">
                <h3 class="">Sign up</h3>
            </div>

            <div class="input-block active">
                <label for="username">Username</label>
                <input type="text" id="username" v-model="username" required>
            </div>

            <div class="input-block active">
                <label for="email">Email</label>
                <input type="email" id="email" v-model="email" required>
            </div>

            <div class="input-block active">
                <label for="password">Password</label>

                <div class="input-group">
                    <input v-bind:type="passwordType" id="password" v-model="password" required>

                    <span v-on:click="togglePassword" v-if="!showPassword">
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-eye-fill" viewBox="0 0 16 16">
                                <path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0" />
                                <path
                                    d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8m8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7" />
                            </svg>
                        </div>
                    </span>

                    <span v-on:click="togglePassword" v-else>
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-eye-slash-fill" viewBox="0 0 16 16">
                                <path
                                    d="m10.79 12.912-1.614-1.615a3.5 3.5 0 0 1-4.474-4.474l-2.06-2.06C.938 6.278 0 8 0 8s3 5.5 8 5.5a7 7 0 0 0 2.79-.588M5.21 3.088A7 7 0 0 1 8 2.5c5 0 8 5.5 8 5.5s-.939 1.721-2.641 3.238l-2.062-2.062a3.5 3.5 0 0 0-4.474-4.474z" />
                                <path
                                    d="M5.525 7.646a2.5 2.5 0 0 0 2.829 2.829zm4.95.708-2.829-2.83a2.5 2.5 0 0 1 2.829 2.829zm3.171 6-12-12 .708-.708 12 12z" />
                            </svg>
                        </div>
                    </span>
                </div>
            </div>

            <div class="input-block active">
                <label for="confirm-password">Confirm password</label>

                <div class="input-group flex-nowrap">
                    <input v-bind:type="passwordType2" id="confirm-password" v-model="confirmPassword" required>

                    <span v-on:click="togglePassword2" v-if="!showPassword2">
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-eye-fill" viewBox="0 0 16 16">
                                <path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0" />
                                <path
                                    d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8m8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7" />
                            </svg>
                        </div>
                    </span>

                    <span v-on:click="togglePassword2" v-else>
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-eye-slash-fill" viewBox="0 0 16 16">
                                <path
                                    d="m10.79 12.912-1.614-1.615a3.5 3.5 0 0 1-4.474-4.474l-2.06-2.06C.938 6.278 0 8 0 8s3 5.5 8 5.5a7 7 0 0 0 2.79-.588M5.21 3.088A7 7 0 0 1 8 2.5c5 0 8 5.5 8 5.5s-.939 1.721-2.641 3.238l-2.062-2.062a3.5 3.5 0 0 0-4.474-4.474z" />
                                <path
                                    d="M5.525 7.646a2.5 2.5 0 0 0 2.829 2.829zm4.95.708-2.829-2.83a2.5 2.5 0 0 1 2.829 2.829zm3.171 6-12-12 .708-.708 12 12z" />
                            </svg>
                        </div>
                    </span>
                </div>
            </div>

            <div class="input-block active">
                <button type="submit">Sign up</button>
            </div>

            <div class="input-block active">
                <p>Already have account <router-link :to="{ name: 'login' }">Log in</router-link></p>
            </div>

            <div v-if="errors" class="errors-block">
                <div v-for="error in errors">
                    <ul>
                        <li>{{ error }}</li>
                    </ul>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Signup',
    data() {
        return {
            passwordType: 'password',
            showPassword: false,
            passwordType2: 'password',
            showPassword2: false,

            username: '',
            email: '',
            password: '',
            confirmPassword: '',

            errors: [],
        }
    },
    methods: {
        togglePassword() {
            this.showPassword = !this.showPassword
            this.passwordType = (this.passwordType == 'password') ? 'text' : 'password'
        },

        togglePassword2() {
            this.showPassword2 = !this.showPassword2
            this.passwordType2 = (this.passwordType2 == 'password') ? 'text' : 'password'
        },

        async signup() {
            if (this.password !== this.confirmPassword) {
                this.errors.push('The passwords must be identical.')
                return 0
            }

            const formData = {
                username: this.username,
                email: this.email,
                password: this.password,
            }


            axios
                .post('users/', formData)
                .then(response => {
                    this.$router.push('/user/log-in/')
                })
                .catch(error => {
                    console.log(error)
                })
        },

        animateBlocks() {
            
            const blocks = document.getElementsByClassName('input-block')
            const arrayBlocks = Array.from(blocks)

            arrayBlocks.forEach((block, i) => {
                setInterval(() => {
                    block.classList.remove('active')
                }, 100 * i)
            })
        }
    },
    mounted() {
        this.animateBlocks()
    }
}
</script>

<style lang="scss">
@import "@/assets/styles/authentication.scss";
</style>