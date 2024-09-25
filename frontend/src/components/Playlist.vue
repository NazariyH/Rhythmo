<template>
    <div class="block active">
        <div class="block-header"><img :src="playlist_thumbnail" alt="image"></div>
        <div class="description">
            <h4>{{ playlist.title }}</h4>
        </div>
        <div class="footer">
            <div>
                <router-link>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-play-fill" viewBox="0 0 16 16">
                        <path
                            d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393" />
                    </svg>
                </router-link>
            </div>
            <div>
                <button class="like" v-if="is_current_user">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-suit-heart-fill" viewBox="0 0 16 16">
                        <path
                            d="M4 1c2.21 0 4 1.755 4 3.92C8 2.755 9.79 1 12 1s4 1.755 4 3.92c0 3.263-3.234 4.414-7.608 9.608a.513.513 0 0 1-.784 0C3.234 9.334 0 8.183 0 4.92 0 2.755 1.79 1 4 1" />
                    </svg>
                </button>

                <button class="trash" v-if="is_current_user">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-trash-fill" viewBox="0 0 16 16">
                        <path
                            d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5M8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5m3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0" />
                    </svg>
                </button>

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
export default {
    name: 'Playlist',
    props: ['playlist', 'is_current_user'],
    data() {
        return {
            playlist_thumbnail: '',
        }
    },
    mounted() {
        this.playlist_thumbnail = `${this.$store.getters.getBaseURL}${this.playlist.playlist_thumbnail}`
    },
}
</script>

<style lang="scss">
.block {
    position: relative;
    width: 280px;
    margin: 20px;

    background-color: antiquewhite;
    transition: all .3s ease-in-out;
    transform: translateX(0);

    &.active {
        transform: translateX(400%) !important;
    }



    .block-header {
        img {
            width: 280px;
            height: 280px;
        }
    }

    div.description {
        display: flex;
        justify-content: start;

        padding: 0 10px;
        h4 {
            align-content: start;    
        }
    }

    div.footer {
        display: flex;
        justify-content: space-between;
        align-items: center;

        padding: 0 10px;
        height: 50px;
        width: 100%;


        button svg {
            width: 14px;
            height: 14px;

            margin-left: 10px;
        }

        a svg {
            width: 25px;
            height: 25px;
        }
    }
}
</style>