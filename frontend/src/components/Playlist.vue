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
                        class="bi bi-suit-heart" viewBox="0 0 16 16">
                        <path
                            d="m8 6.236-.894-1.789c-.222-.443-.607-1.08-1.152-1.595C5.418 2.345 4.776 2 4 2 2.324 2 1 3.326 1 4.92c0 1.211.554 2.066 1.868 3.37.337.334.721.695 1.146 1.093C5.122 10.423 6.5 11.717 8 13.447c1.5-1.73 2.878-3.024 3.986-4.064.425-.398.81-.76 1.146-1.093C14.446 6.986 15 6.131 15 4.92 15 3.326 13.676 2 12 2c-.777 0-1.418.345-1.954.852-.545.515-.93 1.152-1.152 1.595zm.392 8.292a.513.513 0 0 1-.784 0c-1.601-1.902-3.05-3.262-4.243-4.381C1.3 8.208 0 6.989 0 4.92 0 2.755 1.79 1 4 1c1.6 0 2.719 1.05 3.404 2.008.26.365.458.716.596.992a7.6 7.6 0 0 1 .596-.992C9.281 2.049 10.4 1 12 1c2.21 0 4 1.755 4 3.92 0 2.069-1.3 3.288-3.365 5.227-1.193 1.12-2.642 2.48-4.243 4.38z" />
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