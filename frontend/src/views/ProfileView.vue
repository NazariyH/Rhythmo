<template>
    <div class="section">
        <ProfileInfo v-if="!profileNotExist" :profileImage="profileImage" :username="username"
            :age="age" :bio="bio" :gender="gender" :followers="followers" :is_current_user="is_current_user" />
        
        
        <div v-if="!profileNotExist" class="content-block">
            <Song v-for="song in songs" :song="song" :is_current_user="is_current_user" />
        </div>

        <div class="pofile-not-found" v-if="profileNotExist">
            <h1>Profile with this id don't exist</h1>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ProfileInfo from '@/components/ProfileInfo.vue'
import Song from '@/components/Song.vue'
import Playlist from '@/components/Playlist.vue';

export default {
    name: "Profile",
    components: {
        ProfileInfo,
        Song,
    },
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
            profileNotExist: true,

            songs: null,
            playlists: null,
        }
    },
    methods: {
        async fetchProfileData() {
            try {
                const response = await axios.get('user/profile/17/')
                const profileData = response.data.profile

                this.username = profileData.fullName
                this.age = profileData.age
                this.bio = profileData.bio
                this.gender = profileData.gender
                this.followers = profileData.followers.length
                this.is_current_user = response.data.is_current_user
                this.profileImage = `${this.$store.getters.getBaseURL}${profileData.profileImage}`
                this.profileNotExist = false

                
                this.songs = response.data.songs
                console.log(this.songs);

            } catch (error) {
                if (error.status = 404) {
                    this.profileNotExist = false
                }

                console.error('Error fetching profile:', error.response ? error.response.data : error.message)
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
        }
    },
    mounted() {
        this.fetchProfileData().then(() => {
            this.startAnimation()
        })
    },
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

.info-header {
    width: 300px;

    h1 {
        text-align: start;
    }
}

@media(max-width: 800px) {
    .section {
        display: flex;
        align-items: center;
        flex-direction: column;

        div.info-section {
            overflow-y: visible !important;
            height: auto !important;
            margin-bottom: 50px;

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
</style>