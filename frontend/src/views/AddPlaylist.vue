<template>
    <div class="container">
        <form v-on:submit.prevent="addPlaylist">
            <div class="form-title input-block active">
                <h3>Add playlist</h3>
            </div>

            <div class="input-block active">
                <label for="title">Title</label>
                <input type="text" id="title" v-model="title" required>
            </div>

            <div class="input-block active">
                <label for="description">Description</label>
                <input type="text" id="description" v-model="description">
            </div>

            <div class="input-block active buttons">
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
    name: 'AddPlaylist',
    data() {
        return {
            title: '',
            description: '',
            thumbnail: null,
        }
    },
    methods: {
        startAnimation() {
            const blocks = document.getElementsByClassName('input-block')
            const blocks_array = Array.from(blocks)

            blocks_array.forEach((block, i) => {
                setTimeout(() => {
                    block.classList.remove('active')
                }, 100 * i)
            })
        },

        onThumbnailChange(event) {
            this.thumbnail = event.target.files[0]
        },

        async addPlaylist() {
            const token = localStorage.getItem('token')
            if (!token) {
                this.$router.push({ name: 'login' })
                return
            }


            const data = new FormData()
            data.append('title', this.title)
            data.append('description', this.description)
            data.append('playlist_thumbnail', this.thumbnail)

            try {
                const response = await axios.post('playlist/', data, {
                    headers: {
                        'Authorization': `Token ${token}`
                    }
                })

                this.$router.push({ 'name': 'home' })
            } catch (error) {
                console.log(error)
            }
        }
    },
    mounted() {
        this.startAnimation()
    }
}
</script>

<style>
.input-block.buttons label {
    width: 100% !important;
    border-radius: 10px !important;

}
</style>