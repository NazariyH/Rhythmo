<template>
    <div class="section">
        <form @submit.prevent="submitProfile">
            <div class="input-block">
                <div>
                    <label for="username">Your full name</label>
                    <label for="age">Age</label>
                </div>

                <div>
                    <input v-model="username" type="text" id="username" required>
                    <input v-model="age" type="number" id="age" required>
                </div>
            </div>

            <div class="input-block">
                <label for="bio">Your biography</label>
                <textarea id="bio" v-model="bio" maxlength="900"></textarea>
            </div>

            <div class="input-block">
                <select v-model="gender">
                    <option value="MALE">Male</option>
                    <option value="FEMALE">Female</option>
                    <option value="CISGENDER">Cisgender</option>
                    <option value="TRANSGENDER">Transgender</option>
                    <option value="NON-BINARY">Non-Binary</option>
                    <option value="INTERSEX">Intersex</option>
                    <option value="OTHERS">Others</option>
                </select>
            </div>

            <div class="vertical">
                <button type="submit">Save</button>

                <label for="image">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-image" viewBox="0 0 16 16">
                        <path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0" />
                        <path
                            d="M2.002 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2zm12 1a1 1 0 0 1 1 1v6.5l-3.777-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12V3a1 1 0 0 1 1-1z" />
                    </svg>
                </label>

                <input type="file" id="image" v-on:change="onFileChange">
            </div>
        </form>
    </div>
</template>

<script>
    import axios from 'axios'


    export default {
        name: 'ProfileEditView',
        data() {
            return {
                username: '',
                age: null,
                bio: '',
                gender: null,
                profileImage: '',
            }
        },
        methods: {
            onFileChange(event) {
                this.profileImage = event.target.files[0]
            },

            async submitProfile() {
                try {
                    const token = localStorage.getItem('token')

                    const data = new FormData()
                    data.append('fullName', this.username)
                    data.append('age', this.age)
                    data.append('bio', this.bio)
                    data.append('gender', this.gender)
                    data.append('profileImage', this.profileImage)

                    const response = await axios.post('user/profile/', data, {
                        headers: {
                            'Authorization': `Token ${token}`,
                            'Content-Type': 'multipart/form-data',                        
                        }
                    })

                    console.log('Profile submitted successfully:', response.data)
                } catch (error) {
                    console.error('Error submitting profile:', error)
                }
            },
        }
    }
</script>

<style>
    @import "@/assets/styles/profile.scss";
    @import "@/assets/styles/authentication.scss";
</style>