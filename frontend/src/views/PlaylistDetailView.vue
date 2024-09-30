<template>
    <div class="section">
        <div class="playlist-info">
            <div class="info-header">
                <div class="image-wrap">
                    <img :src="playlist_thumbnail" alt="playlist thumbnail">
                </div>
            </div>

            <hr>

            <div class="info-content">
                <div>
                    <h1 v-if="playlist">{{ playlist.title }}</h1>
                    <h1 v-else>Loading...</h1>

                    <router-link v-if="playlist && playlist.id"
                        :to="{ name: 'edit-playlist', params: { id: playlist.id } }">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-pencil-fill" viewBox="0 0 16 16">
                            <path
                                d="M12.854.146a.5.5 0 0 0-.707 0L10.5 1.793 14.207 5.5l1.647-1.646a.5.5 0 0 0 0-.708zm.646 6.061L9.793 2.5 3.293 9H3.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.207zm-7.468 7.468A.5.5 0 0 1 6 13.5V13h-.5a.5.5 0 0 1-.5-.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.5-.5V10h-.5a.5.5 0 0 1-.175-.032l-.179.178a.5.5 0 0 0-.11.168l-2 5a.5.5 0 0 0 .65.65l5-2a.5.5 0 0 0 .168-.11z" />
                        </svg>
                    </router-link>
                </div>

                <div>
                    <h4>likes:</h4>
                    <button class="like" v-if="!is_current_user" v-on:click="likeOrUnlikePlaylist">
                        <span>{{ playlist_likes_count }}</span>

                        <svg v-if="!playlist_is_liked" xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                            fill="currentColor" class="bi bi-suit-heart" viewBox="0 0 16 16">
                            <path
                                d="m8 6.236-.894-1.789c-.222-.443-.607-1.08-1.152-1.595C5.418 2.345 4.776 2 4 2 2.324 2 1 3.326 1 4.92c0 1.211.554 2.066 1.868 3.37.337.334.721.695 1.146 1.093C5.122 10.423 6.5 11.717 8 13.447c1.5-1.73 2.878-3.024 3.986-4.064.425-.398.81-.76 1.146-1.093C14.446 6.986 15 6.131 15 4.92 15 3.326 13.676 2 12 2c-.777 0-1.418.345-1.954.852-.545.515-.93 1.152-1.152 1.595zm.392 8.292a.513.513 0 0 1-.784 0c-1.601-1.902-3.05-3.262-4.243-4.381C1.3 8.208 0 6.989 0 4.92 0 2.755 1.79 1 4 1c1.6 0 2.719 1.05 3.404 2.008.26.365.458.716.596.992a7.6 7.6 0 0 1 .596-.992C9.281 2.049 10.4 1 12 1c2.21 0 4 1.755 4 3.92 0 2.069-1.3 3.288-3.365 5.227-1.193 1.12-2.642 2.48-4.243 4.38z" />
                        </svg>

                        <svg v-else xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-suit-heart-fill" viewBox="0 0 16 16">
                            <path
                                d="M4 1c2.21 0 4 1.755 4 3.92C8 2.755 9.79 1 12 1s4 1.755 4 3.92c0 3.263-3.234 4.414-7.608 9.608a.513.513 0 0 1-.784 0C3.234 9.334 0 8.183 0 4.92 0 2.755 1.79 1 4 1" />
                        </svg>
                    </button>
                    <span v-else>{{ playlist_likes_count }}</span>
                </div>

                <div>
                    <h4>Created on</h4>
                    <h4 v-if="playlist">{{ created_on }}</h4>
                    <h4 v-else>Loading...</h4>
                </div>

                <div>
                    <h4>Created by</h4>
                    <h4 v-if="playlist">{{ playlist.author }}</h4>
                    <h4 v-else>Loading...</h4>
                </div>

                <hr>

                <div class="description" v-if="playlist">
                    <p>{{ playlist.description }}</p>
                </div>
            </div>
        </div>

        <div class="content-section">
            <div v-if="songs" v-for="song in songs">
                <Song :song="song" :is_current_user="is_current_user" />
            </div>
            <div v-else>Loading...</div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Song from '@/components/Song.vue'

export default {
    data() {
        return {
            playlist: null,
            playlist_thumbnail: null,
            playlist_likes_count: 0,
            playlist_is_liked: false,
            created_on: null,
            is_current_user: false,
            songs: null,
        }
    },
    components: {
        Song,
    },
    methods: {
        async fetchPlaylistData() {
            try {
                const response = await axios.get(`playlist/${this.$route.params.id}/detail/`)

                this.playlist = response.data.playlist
                this.is_current_user = response.data.is_current_user
                this.playlist_is_liked = response.data.playlist_is_liked

                if (response.data.songs) {
                    console.log(response.data.songs)
                    this.songs = response.data.songs
                }


                if (this.playlist) {
                    this.playlist_thumbnail = `${this.$store.getters.getBaseURL}${this.playlist.playlist_thumbnail}`
                    this.playlist_likes_count = this.playlist.likes.length

                    let date = new Date(this.playlist.created_on)
                    this.created_on = date.toISOString().split('T')[0]
                }

            } catch (error) {
                console.log(error)
            }
        },

        async likeOrUnlikePlaylist() {
            const token = localStorage.getItem('token')
            if (!token) {
                this.$router.push({ 'name': 'login' })
                return
            }

            try {
                const response = await axios.patch(`playlist/${this.playlist.id}/like-or-dislike/`, null, {
                    headers: {
                        'Authorization': `Token ${this.$store.state.token}`,
                    }
                })


                this.playlist_is_liked = response.data.playlist_is_liked
                this.playlist_likes_count = response.data.playlist_likes_length
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
    },
    mounted() {
        this.fetchPlaylistData().then(() => {
            this.startAnimation()
        })
    }
}
</script>

<style lang="scss">
.playlist-info {
    min-width: 400px;
    max-width: 400px;
    overflow-y: auto;
    padding: 0 20px;

    border-right: 0.5x solid #000000 !important;

    .info-header .image-wrap img {
        position: relative;
        width: 300px;
        height: 300px;
        // border-radius: 50%;
        overflow: hidden;
    }

    .info-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;

        div {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;

            &.description {
                text-align: start;
                width: 300px;
                padding: 10px;
                margin-bottom: 20px !important;
                background-color: #ffffff;
            }
        }

        div:nth-child(2),
        div:nth-child(3),
        div:nth-child(4) {
            margin: 15px 0;

            button {
                display: flex;
                justify-content: center;
                align-items: center;

                span {
                    margin-right: 10px;
                }
            }
        }
    }

    .card:nth-child(1) {
        margin-top: 0px !important;
    }
}
</style>