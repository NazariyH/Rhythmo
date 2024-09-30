<template>
    <div class="section">
        <form @submit.prevent="submitPlaylist">
            <div class="form-title input-block active">
                <h3>Edit playlist</h3>
            </div>

            <div class="input-block active">
                <label for="title">title</label>
                <input type="text" v-model="title" id="title">
            </div>

            <div class="input-block active">
                <label for="description">Description</label>
                <textarea id="description" v-model="description" maxlength="900"></textarea>
            </div>

            <div class="input-block active">
                <div class="vertical">
                    <button type="submit">Save</button>

                    <label v-if="!playlist_thumbnail" for="image">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-image" viewBox="0 0 16 16">
                            <path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0" />
                            <path
                                d="M2.002 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2zm12 1a1 1 0 0 1 1 1v6.5l-3.777-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12V3a1 1 0 0 1 1-1z" />
                        </svg>
                    </label>

                    <button v-else v-on:click="resetPlaylistThumbnail" class="resetImage">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-image" viewBox="0 0 16 16">
                            <path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0" />
                            <path
                                d="M2.002 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2zm12 1a1 1 0 0 1 1 1v6.5l-3.777-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12V3a1 1 0 0 1 1-1z" />
                        </svg>
                    </button>

                    <input type="file" id="image" v-on:change="onFileChange">
                </div>
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
            title: '',
            description: '',
            playlist_thumbnail: '',
        }
    },
    methods: {
        onFileChange(event) {
            this.playlist_thumbnail = event.target.files[0]
        },

        resetPlaylistThumbnail() {
            this.playlist_thumbnail = ''
        },

        async fetchProfile() {
            const token = localStorage.getItem('token')

            if (!token) {
                console.log('Token not found')
                return
            }
            try {
                const response = await axios.get(`playlist/${this.$route.params.id}/detail/`)

                this.title = response.data.playlist.title
                this.description = response.data.playlist.description
            } catch (error) {
                console.log(error)
            }
        },

        async submitPlaylist() {
            try {
                const token = localStorage.getItem('token')

                const data = new FormData()
                data.append('title', this.title)
                data.append('description', this.description)
                data.append('playlist_thumbnail', this.playlist_thumbnail)

                const response = await axios.post(`playlist/${this.$route.params.id}/detail/`, data, {
                    headers: {
                        'Authorization': `Token ${token}`,
                        'Content-Type': 'multipart/form-data',
                    }
                })

                this.$router.push({ 'name': 'playlist-detail', params: { id: this.$route.params.id } })
            } catch (error) {
                console.error('Error submitting profile:', error)
            }
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
        this.fetchProfile()
        this.animateBlocks()
    },
}
</script>

<style lang="scss"> 
form {
    overflow: hidden;

    label {
        margin: 0 !important;
    }
}

.input-block {
    transform: translateX(0) !important;
    transition: all .3s ease-out;

    &.active {
        transform: translateX(200%) !important;
    }
}
</style>