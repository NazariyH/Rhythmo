<template>
    <div class="card active">
        <div class="info">
            <div>
                <img v-bind:src="song.thumbnail">
                <div>
                    <h4>{{ song.name }}</h4>
                    <router-link to="">{{ song.author }}</router-link>
                </div>
            </div>
        </div>

        <div class="player">
            <button class="play">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                     class="bi bi-play-fill" viewBox="0 0 16 16">
                    <path
                        d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393"/>
                </svg>
            </button>

            <input type="range" value="0" id="progres">

            <button class="like">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                     class="bi bi-suit-heart-fill" viewBox="0 0 16 16">
                    <path
                        d="M4 1c2.21 0 4 1.755 4 3.92C8 2.755 9.79 1 12 1s4 1.755 4 3.92c0 3.263-3.234 4.414-7.608 9.608a.513.513 0 0 1-.784 0C3.234 9.334 0 8.183 0 4.92 0 2.755 1.79 1 4 1"/>
                </svg>
            </button>

            <button class="addToPlaylist">
                <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true"
                     xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"
                     viewBox="0 0 24 24">
                    <path
                        d="M7.833 2c-.507 0-.98.216-1.318.576A1.92 1.92 0 0 0 6 3.89V21a1 1 0 0 0 1.625.78L12 18.28l4.375 3.5A1 1 0 0 0 18 21V3.889c0-.481-.178-.954-.515-1.313A1.808 1.808 0 0 0 16.167 2H7.833Z"/>
                </svg>
            </button>

            <button>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                     class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                    <path
                        d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"/>
                </svg>
            </button>
        </div>
    </div>
</template>

<script>
export default {
    props: ["song"],
    data() {
        return {}
    },
}
</script>

<style lang="scss">
.card {
    padding: 10px 30px;
    background-color: #ffffff;

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

        button {
            display: flex;
            align-items: center;

            svg {
                width: 15px;
                height: 15px;
                color: #795757;
            }

            &.like, &.addToPlaylist {
                margin-right: 10px;
            }

            &.play svg {
                width: 20px;
                height: 20px;
            }
        }

        input[type="range"] {
            width: 100%;
            height: 7px;
            margin: 0 20px;

            -webkit-appearance: none;
            background: linear-gradient(135deg, #FAEBD7, #FFF5E1, #F0E2D1);
        }

        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;

            background-color: #795757;
            width: 15px;
            height: 15px;

            border-radius: 50%;
        }
    }

    &.active {
        transform: translateX(100%);
    }
}
</style>