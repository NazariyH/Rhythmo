<template>
    <div class="container">
        <form v-on:submit.prevent="login">
            <div class="form-title">
                <h3>Log in</h3>
            </div>

            <div class="input-block">
                <label for="username">Username</label>
                <input type="text" v-model="username" id="username" required>
            </div>

            <div class="input-block">
                <label for="password">Password</label>

                <div class="input-group flex-nowrap">
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

            <button type="submit">Log in</button>

            <div>
                <p>Don't have an account? <router-link :to="{ name: 'signup' }">Let's get start</router-link></p>
            </div>

            <div v-if="errors.length" class="errors-block">
                <ul>
                    <li v-for="error in errors">{{ error }}</li>
                </ul>
            </div>
        </form>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    name: 'Login',
    data() {
        return {
            passwordType: 'password',
            showPassword: false,

            username: '',
            password: '',
            errors: [],
            is_authenticated: false,
        }
    },
    methods: {
        togglePassword() {
            this.showPassword = !this.showPassword;
            this.passwordType = (this.passwordType === 'password') ? 'text' : 'password';
        },
        async login() {
            const formData = {
                username: this.username,
                password: this.password,
            }

            try {
                const response = await axios.post('token/login', formData, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })

                const token = response.data.auth_token

                if (token) {
                    this.$store.commit('setToken', token)
                    this.isAuthenticated = true

                    axios.defaults.headers.common['Authorization'] = `Token ${token}`

                    localStorage.setItem("token", token)
                    localStorage.setItem("auth_status", "true")

                    this.$router.push('/')
                } else {
                    this.errors.push('Login failed: No token received')
                }
                
                this.$router.push('/')
                    .then(() => {
                        this.$nextTick(() => {
                            window.location.reload()
                        })
                    })

            } catch (error) {
                this.errors = error.response ? error.response.data : ['An unexpected error occurred']
            }
        }

    },
}
</script>

<style lang="scss">
@import "@/assets/styles/authentication.scss";
</style>