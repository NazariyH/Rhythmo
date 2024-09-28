<template>
    <div class="card active" :data-songBlockId="song.id">
        <div class="info">
            <div>
                <img v-bind:src="song_thumbnail_url">
                <div>
                    <h4>{{ song.name }}</h4>
                    <router-link to="">{{ song.author }}</router-link>
                </div>
            </div>
        </div>

        <audio class="song d-none" :data-songId="song.id" controls>
            <source :src="song_url">
        </audio>

        <div class="player">
            <div class="play">
                <button :data-songBtnId="song.id" v-if="!playing" v-on:click="playPause">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-play-fill" viewBox="0 0 16 16">
                        <path
                            d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393" />
                    </svg>
                </button>
                <button :data-songBtnId="song.id" v-else v-on:click="playPause">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-pause-fill" viewBox="0 0 16 16">
                        <path
                            d="M5.5 3.5A1.5 1.5 0 0 1 7 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5m5 0A1.5 1.5 0 0 1 12 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5" />
                    </svg>
                </button>
            </div>

            <div class="count">
                <span>15:</span><span>50</span>
            </div>

            <input type="range" v-model="current_progress_value" value="0" class="progress active"
                :data-songProgressId="song.id" v-on:input="updateCurrentMusicTime">

            <div class="like">
                <button v-on:click="likeOrUnlikeSong" :data-songId="song.id" v-if="!is_current_user">
                    <span>{{ current_song_likes_length }}</span>
                    
                    <svg v-if="!song_is_liked" xmlns="http://www.w3.org/2000/svg" width="16" height="16"
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
            </div>

            <div class="trash">
                <button v-if="is_current_user" :data-songId="song.id" v-on:click="removeSong">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-trash-fill" viewBox="0 0 16 16">
                        <path
                            d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5M8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5m3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0" />
                    </svg>
                </button>
            </div>

            <div class="addToPlaylist">
                <button>
                    <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"
                        viewBox="0 0 24 24">
                        <path
                            d="M7.833 2c-.507 0-.98.216-1.318.576A1.92 1.92 0 0 0 6 3.89V21a1 1 0 0 0 1.625.78L12 18.28l4.375 3.5A1 1 0 0 0 18 21V3.889c0-.481-.178-.954-.515-1.313A1.808 1.808 0 0 0 16.167 2H7.833Z" />
                    </svg>
                </button>
            </div>

            <div>
                <button>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                        <path
                            d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2" />
                    </svg>
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    props: ["song", "is_current_user"],
    data() {
        return {
            song_url: '',
            song_thumbnail_url: '',

            playing: false,
            current_music: null,
            current_progress: null,
            current_progress_value: 0,
            current_progress_value: 0,

            current_song_likes_length: 0,
            final_song_likes_length: 0,
            song_is_liked: false,
        }
    },
    methods: {
        playPause(event) {
            this.current_song_id = event.currentTarget.getAttribute('data-songBtnId')
            this.current_progress = document.querySelector(`[data-songProgressId="${this.current_song_id}"]`)
            this.current_music = document.querySelector(`[data-songId="${this.current_song_id}"]`)


            this.playing ? this.current_music.pause() : this.current_music.play()

            if (!this.playing) {
                setInterval(() => {
                    this.current_progress_value = Math.round(100 * this.current_music.currentTime / this.current_music.duration)
                    this.current_progress.value = this.current_progress_value

                }, 1000)
            }

            this.playing = !this.playing
        },

        updateCurrentMusicTime(event) {
            this.current_song_id = event.currentTarget.getAttribute('data-songProgressId')
            this.current_music = document.querySelector(`[data-songId="${this.current_song_id}"]`)

            this.current_music.currentTime = this.current_music.duration * event.currentTarget.value / 100
        },

        async removeSong(event) {
            try {
                const response = await axios.delete(`song/remove/${this.song.id}/`)
                document.querySelector(`[data-songBlockId="${songId}"]`).remove()
            } catch (error) {
                console.log(error)
            }
        },

        async checkSongReactionStatus() {
            const token = localStorage.getItem('token')
            try {
                const response = await axios.get(`song/${this.song.id}/like/check/`, {
                    headers: {
                        'Authorization': `Token ${token}`
                    }
                })

                this.song_is_liked = response.data.song_is_liked
            } catch (error) {
                console.log(error)
            }
        },

        async likeOrUnlikeSong() {
            const token = localStorage.getItem('token')
            !token && this.$router.push({ 'name': 'login' })

            try {
                const response = await axios.patch(`song/${this.song.id}/like-or-dislike/`, null, {
                    headers: {
                        'Authorization': `Token ${this.$store.state.token}`,
                    }
                })

                this.song_is_liked = response.data.song_is_liked
                this.current_song_likes_length = response.data.song_likes_length
                this.final_song_likes_length = response.data.song_likes_length
            } catch (error) {
                console.log(error)
            }
        },

        startLikeCountAnimation() {
            for (let i = 0; i < this.final_song_likes_length + 1; i++) {
                setTimeout(() => {
                    this.current_song_likes_length = i
                }, 150 * i)
            }
        },
    },
    mounted() {
        this.song_url = `${this.$store.getters.getBaseURL}${this.song.song}`
        this.song_thumbnail_url = `${this.$store.getters.getBaseURL}${this.song.song_thumbnail}`
        this.final_song_likes_length = this.song.likes.length

        this.checkSongReactionStatus().then(() => {
            this.startLikeCountAnimation()
        })
    }
}
</script>

<style lang="scss">
.card {
    padding: 10px 30px;
    background-color: #ffffff;
    margin: 5px 0;

    transition: all .3s ease-in-out;

    .info {
        display: flex;

        div {
            display: flex;
            align-items: start;

            height: 60px;
            position: relative;

            img {
                width: 60px;
                height: 60px;

            }

            div {
                display: flex;
                justify-content: center;
                flex-direction: column;

                margin-left: 10px;

                a {
                    font-size: 12px;
                    color: #0000EE;
                }
            }
        }
    }

    .player {
        display: flex;
        align-items: center;
        margin-top: 20px;

        div {
            position: relative;
            width: 15px;
            height: 15px;

            &.addToPlaylist,
            &.trash {
                margin-right: 10px;
            }

            &.play svg {
                width: 20px;
                height: 20px;
            }

            button {
                position: absolute;
                top: 50%;
                left: 50%;

                transform: translate(-50%, -50%);
                z-index: 10;

                display: flex;
                align-items: center;

                svg {
                    width: 15px;
                    height: 15px;
                    color: #795757;
                }
            }
        }

        .count {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0 20px;
        }

        input[type="range"] {
            width: 100%;
            height: 7px;
            margin: 0 20px;

            -webkit-appearance: none;
            background: linear-gradient(135deg, #FAEBD7, #FFF5E1, #F0E2D1);
            transition: all .5s ease-in-out;

            &.active {
                transform: translateX(150%);
            }
        }

        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;

            background-color: #795757;
            width: 15px;
            height: 15px;

            border-radius: 50%;
        }
    }

    button span {
        margin-right: 10px
    }

    &.active {
        transform: translateX(100%);
    }

    .d-none {
        display: none;
    }
}
</style>