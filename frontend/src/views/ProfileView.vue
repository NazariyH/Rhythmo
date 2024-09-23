<template>
    <div class="section">
        <ProfileInfo v-if="isAuthenticated && !profileNotExist" :profileImage="profileImage" :username="username"
                     :age="age" :bio="bio"
                     :gender="gender" :followers="followers"/>
        <div v-if="isAuthenticated && !profileNotExist" class="content-block">
            <div v-if="loading" class="loading">
                <span></span>
            </div>
            <Song v-for="song in songs" v-else :song="song"/>
        </div>

        <div class="pofile-not-found" v-if="!isAuthenticated">
            <h1>You're not authenticated.</h1>
            <button>
                <router-link :to="{ name: 'login' }">Log in</router-link>
            </button>
        </div>
        <div class="pofile-not-found" v-if="profileNotExist">
            <h1>You don't have an account</h1>
            <button>
                <router-link :to="{ name: 'profile-edit' }">Create</router-link>
            </button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ProfileInfo from '@/components/ProfileInfo.vue'
import Song from '@/components/Song.vue'

export default {
    name: 'Profile',
    data() {
        return {
            username: '',
            age: null,
            bio: '',
            gender: '',
            followers: 0,
            profileImage: '',

            isAuthenticated: false,
            profileNotExist: false,

            songs: null,
            loading: true,
        };
    },
    components: {
        ProfileInfo,
        Song,
    },
    methods: {
        async fetchProfileData() {
            const token = localStorage.getItem('token')

            if (token) {
                axios.defaults.headers.common['Authorization'] = 'Token ' + token
                this.isAuthenticated = true

                try {
                    const response = await axios.get('user/profile/')
                    const profileData = response.data.profile

                    this.username = profileData.fullName
                    this.age = profileData.age
                    this.bio = profileData.bio
                    this.gender = profileData.gender
                    this.followers = profileData.followers.length
                    this.profileImage = `http://localhost:8000${profileData.profileImage}`

                } catch (error) {
                    if (error.status = 404) {
                        this.profileNotExist = true
                    }

                    console.error('Error fetching profile:', error.response ? error.response.data : error.message)
                }
            } else {
                console.error('No authentication token found.')
            }
        },

        async fetchSongData() {
            const token = localStorage.getItem('token')

            if (!token) {
                console.log('Token not found')
                return
            }

            try {
                const response = await axios.get('song/', {
                    headers: {
                        'Authorization': `Token ${token}`
                    }
                })

                this.songs = response.data.songs
            } catch(error) {
                console.log(error)
            }
        },

        startAnimation() {
            const songs = document.getElementsByClassName('card')
            const inputRange = document.getElementsByClassName('progres')

            const songArray = Array.from(songs)
            const inputRangeArray = Array.from(inputRange)

            songArray.forEach((song, i) => {
                setTimeout(() => {
                    song.classList.remove('active')
                }, 80 * i)

                setTimeout(() => {
                    inputRangeArray[i].classList.remove('active')
                }, 120 * i)
            })
        }
    },
    mounted() {
        this.fetchProfileData()
        this.fetchSongData()

        this.startAnimation()

        this.$nextTick(() => {
            setInterval(() => {
                this.fetchSongData()
                this.startAnimation()
                this.loading = false
            }, 3000)
            this.startAnimation()
        })
    }
}
</script>

<style lang="scss">
hr {
    border: 0.5px solid #c6c6c6;
    width: 100%;
    margin: 30px 0;
}

.section {
    position: relative;
    width: 100%;
    height: 80vh;
}

.section .pofile-not-found {
    position: absolute;
    top: 50%;
    left: 50%;

    transform: translate(-50%, -50%);
}

.section .pofile-not-found button {
    background-color: antiquewhite;
    width: 150px;
    height: 35px;
    border-radius: 10px;

    transition: all .3s ease-out;
}

.section .pofile-not-found button:hover {
    background-color: #ffffff;
}

.content-block {
    width: 100%;
}

.loading {
    display: flex;
    justify-content: center;
    align-items: center;

    height: 100vh;

    span {
        width: 50px;
        height: 50px;

        border-radius: 50%;
    }
}
</style>
