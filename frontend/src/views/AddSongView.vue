<template>
    <div class="container">
        <form v-on:submit.prevent="addSong">
            <div class="form-title input-block active">
                <h3>Add song</h3>
            </div>

            <div class="input-block active">
                <label for="name">Name</label>
                <input type="text" id="name" v-model="name" required>
            </div>

            <div class="input-block active buttons">
                <label for="song" id="songBtn">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-music-note" viewBox="0 0 16 16">
                        <path d="M9 13c0 1.105-1.12 2-2.5 2S4 14.105 4 13s1.12-2 2.5-2 2.5.895 2.5 2" />
                        <path fill-rule="evenodd" d="M9 3v10H8V3z" />
                        <path d="M8 2.82a1 1 0 0 1 .804-.98l3-.6A1 1 0 0 1 13 2.22V4L8 5z" />
                    </svg>
                </label>

                <input type="file" id="song" v-on:input="onSongChange" required>

                <label id="thumbnailBtn" for="thumbnail">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-image" viewBox="0 0 16 16">
                        <path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0" />
                        <path
                            d="M2.002 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2zm12 1a1 1 0 0 1 1 1v6.5l-3.777-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12V3a1 1 0 0 1 1-1z" />
                    </svg>
                </label>

                <input type="file" id="thumbnail" v-on:input="onThumbnailChange">
            </div>

            <div class="input-block active">
                <button type="submit">Add</button>
            </div>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            name: '',
            song: null,
            image: null,
        }
    },
    methods: {
        async addSong() {
            const data = new FormData()
            const token = localStorage.getItem('token')

            if (!token) {
                console.log('Token not found')
                return
            }

            data.append('name', this.name)
            data.append('song', this.song)
            data.append('song_thumbnail', this.image)

            try {
                const response = await axios.post('song/', data, {
                    headers: {
                        'Authorization': `Token ${token}`
                    }
                })

                this.$router.push('/')
            } catch (error) {
                console.log(error)
            }
        },

        onSongChange(event) {
            this.song = event.target.files[0]
        },

        onThumbnailChange(event) {
            this.image = event.target.files[0]
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

.input-block {
    &.buttons {
        display: flex;
        flex-direction: row !important;
        justify-content: space-between;

        label {
            display: flex;
            justify-content: center;
            align-items: center;

            color: #000000;
            background-color: #fcf4ea !important;
            transition: all .3s ease-in-out;

            border-radius: 20px;
            width: 50%;
            height: 30px;
        }

        label:hover {
            background-color: #ffffff !important;
        }

        label#songBtn {
            border-radius: 20px 0 0 20px;
            border-right: .5px solid #000000;
        }

        label#thumbnailBtn {
            border-radius: 0 20px 20px 0;
        }


    }

    input[type="file"] {
        display: none;
    }

    button[type="submit"] {
        background-color: #fcf4ea;
        transition: all .3s ease-in-out;
        color: #000000;
    }

    button[type="submit"]:hover {
        background-color: #ffffff;
    }
}
</style>