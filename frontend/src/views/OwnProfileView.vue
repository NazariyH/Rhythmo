<template>
    <div class="section">
        <ProfileInfo v-if="isAuthenticated && !profileNotExist" :profileImage="profileImage" :username="username"
            :age="age" :bio="bio" :gender="gender" :followers="followers" :is_current_user="is_current_user" />

        <div class="content-section">
            <div v-if="isAuthenticated && !profileNotExist" class="playlist-block">
                <Playlist v-for="playlist in playlists" :playlist="playlist" :is_current_user="is_current_user" />
            </div>

            <div v-if="isAuthenticated && !profileNotExist" class="content-block">
                <Song v-for="song in songs" :song="song" :is_current_user="is_current_user" />
            </div>
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
import Playlist from '@/components/Playlist.vue'

export default {
    name: 'OwnProfile',
    data() {
        return {
            username: '',
            age: null,
            bio: '',
            gender: '',
            followers: 0,
            profileImage: '',
            is_current_user: false,

            isAuthenticated: false,
            profileNotExist: false,

            songs: null,
            playlists: null,
        };
    },
    components: {
        ProfileInfo,
        Song,
        Playlist,
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
                    this.is_current_user = response.data.is_current_user
                    this.profileImage = `${this.$store.getters.getBaseURL}${profileData.profileImage}`

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
            } catch (error) {
                console.log(error)
            }
        },

        async fetchPlaylistData() {
            const token = localStorage.getItem('token')

            if (!token) {
                console.log('Token not found')
                return
            }

            try {
                const response = await axios.get('playlist/', {
                    headers: {
                        'Authorization': `Token ${token}`
                    }
                })

                this.playlists = response.data.playlists
            } catch (error) {
                console.log(error)
            }
        },

        startAnimation() {
            const songs = document.getElementsByClassName('card')
            const inputRange = document.getElementsByClassName('progress')

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
        },

        startPlaylistAntimation() {
            const playlists = document.getElementsByClassName('block')
            const playlistArray = Array.from(playlists)

            playlistArray.forEach((playlist, i) => {
                setTimeout(() => {
                    playlist.classList.remove('active')
                }, 300 * i)
            })
        }
    },
    mounted() {
        this.fetchProfileData()


        this.fetchSongData().then(() => {
            this.startAnimation()
        })

        this.fetchPlaylistData().then(() => {
            this.startPlaylistAntimation()
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

.content-block,
.playlist-block {
    width: 100%;
}

.content-section {
    overflow-y: auto;
    overflow-x: hidden !important;
    height: 100vh;

    .content-block {
        overflow: visible !important;
    }
}

.playlist-block {
    display: flex;
    flex-wrap: wrap;

    position: relative;
}

.content-section {
    display: flex;
    flex-direction: column;

    width: 100%;
}

@media(max-width: 800px) {
    .section {
        display: flex;
        align-items: center;
        flex-direction: column;
        height: auto !important;

        div.content-section {
            height: auto !important;
        }

        div.info-section {
            overflow-y: visible !important;
            height: auto !important;
            margin-bottom: 50px;

            .info-header, .bio {
                width: 100% !important;
                padding: 0 30px;
            }


            display: flex;
            flex-direction: column;
            align-items: center;

            border-right: none !important;
        }

        div.content-block {
            overflow-y: visible !important;
            height: auto !important;
        }
    }
}

@media(max-width: 1360px) {
    .playlist-block {
            justify-content: center;
    }
}
</style>
