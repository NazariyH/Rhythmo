<template>
    <nav class="navbar">
        <div>
            <div class="navbar-brand">
                <router-link to="/">Rhythmo</router-link>
            </div>
            <div class="navbar-menu">
                <ul>
                    <li v-if="isAuthenticated">
                        <router-link :to="{ name: 'add-song' }">Add song</router-link>
                    </li>
                    <li v-else>
                        <router-link :to="{ name: 'login' }">Add song</router-link>
                    </li>
                    <li v-if="isAuthenticated">
                        <router-link :to="{ name: 'add-playlist' }">Add playlist</router-link>
                    </li>
                    <li v-else>
                        <router-link :to="{ name: 'login' }">Add song</router-link>
                    </li>
                </ul>
            </div>
        </div>

        <form class="search-form" action="#">
            <input class="form-control me-2" type="text" v-bind:placeholder="finalMessage" v-on:input="getResult"
                v-model="searchQuery">
            <button id="searchButton" type="submit">
                <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                    width="24" height="24" fill="none" viewBox="0 0 24 24">
                    <path stroke="currentColor" stroke-linecap="round" stroke-width="2"
                        d="m21 21-3.5-3.5M17 10a7 7 0 1 1-14 0 7 7 0 0 1 14 0Z" />
                </svg>
            </button>
        </form>

        <div class="icons-menu">
            <ul>
                <li v-if="!isAuthenticated">
                    <router-link :to="{ name: 'login' }">Log in</router-link>
                </li>
                <li v-else>
                    <button v-on:click="logout">Log out</button>
                </li>

                <li>
                    <router-link to="/user/profile">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-person-fill" viewBox="0 0 16 16">
                            <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6" />
                        </svg>
                    </router-link>
                </li>

                <li>
                    <router-link>
                        <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"
                            viewBox="0 0 24 24">
                            <path
                                d="M7.833 2c-.507 0-.98.216-1.318.576A1.92 1.92 0 0 0 6 3.89V21a1 1 0 0 0 1.625.78L12 18.28l4.375 3.5A1 1 0 0 0 18 21V3.889c0-.481-.178-.954-.515-1.313A1.808 1.808 0 0 0 16.167 2H7.833Z" />
                        </svg>
                    </router-link>
                </li>
            </ul>
        </div>

        <div id="searchBlock">
            <div class="search-block-wrap" v-if="!songs.length && !playlists.length && !profiles.length" style="justify-content: center;">
                <h3>We can't find anything :(</h3>
            </div>

            <div class="search-block-wrap" v-else>
                <Song v-for="song in songs" :song="song" :searchView="true" />

                <div class="playlist-wrap">
                    <Playlist v-for="playlist in playlists" :playlist="playlist" :searchView="true" />
                </div>

                <div class="profile-wrap">
                    <div class="block" v-for="profile in profiles" :key="profile.user">
                        <img :src="`${url}/${profile.profileImage}`" alt="profile">

                        <router-link :to="{ name: 'profile', params: { id: profile.user } }">
                            {{ profile.fullName.slice(0, 5) + '..' }}
                        </router-link>
                    </div>
                </div>
            </div>
        </div>

        <div class="vertical-menu-btn" v-on:click="activateBtnMenu">
            <div>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>

        <div class="vertical-menu">
            <form class="vertical-search-form">
                <input class="form-control me-2" type="text" v-bind:placeholder="finalMessage" v-on:input="getResult"
                    v-model="searchQuery">
                <button id="searchButton" type="submit">
                    <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                        <path stroke="currentColor" stroke-linecap="round" stroke-width="2"
                            d="m21 21-3.5-3.5M17 10a7 7 0 1 1-14 0 7 7 0 0 1 14 0Z" />
                    </svg>
                </button>
            </form>

            <div class="vertical-navbar-menu">
                <ul>
                    <li v-if="isAuthenticated">
                        <router-link :to="{ name: 'add-song' }">Add song</router-link>
                    </li>
                    <li v-else>
                        <router-link :to="{ name: 'login' }">Add song</router-link>
                    </li>

                    <li v-if="isAuthenticated">
                        <router-link :to="{ name: 'add-playlist' }">Add playlist</router-link>
                    </li>
                    <li v-else>
                        <router-link :to="{ name: 'login' }">Add song</router-link>
                    </li>
                </ul>
            </div>

            <div class="vertical-icons-menu">
                <ul>
                    <li v-if="!isAuthenticated">
                        <router-link :to="{ name: 'login' }">Log in</router-link>
                    </li>
                    <li v-else>
                        <button v-on:click="logout">Log out</button>
                    </li>

                    <li>
                        <router-link to="/user/profile">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-person-fill" viewBox="0 0 16 16">
                                <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6" />
                            </svg>
                        </router-link>
                    </li>

                    <li>
                        <router-link>
                            <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"
                                viewBox="0 0 24 24">
                                <path
                                    d="M7.833 2c-.507 0-.98.216-1.318.576A1.92 1.92 0 0 0 6 3.89V21a1 1 0 0 0 1.625.78L12 18.28l4.375 3.5A1 1 0 0 0 18 21V3.889c0-.481-.178-.954-.515-1.313A1.808 1.808 0 0 0 16.167 2H7.833Z" />
                            </svg>
                        </router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
import axios from 'axios'
import store from '@/store'
import Song from '@/components/Song.vue'
import Playlist from '@/components/Playlist.vue'

export default {
    name: "Navbar",
    components: {
        Song,
        Playlist,
    },
    data() {
        return {
            message: 'Search for music and playlists ...',
            finalMessage: '',
            username: '',
            isAuthenticated: false,
            searchQuery: '',

            songs: [],
            playlists: [],
            profiles: [],
            url: '',
        }
    },
    methods: {
        activateBtnMenu() {
            let verticalMenuBtn = document.getElementsByClassName("vertical-menu-btn")[0]
            let verticalMenu = document.getElementsByClassName("vertical-menu")[0]

            verticalMenuBtn.classList.toggle('active')
            verticalMenu.classList.toggle('active')
        },

        searchFieldAnimation() {
            this.finalMessage = ''
            let interval = 70


            for (let i = 0; i < this.message.length * 2; i++) {
                setTimeout(() => {
                    if (i >= this.message.length) {
                        this.finalMessage = this.finalMessage.slice(0, this.finalMessage.length - 1)
                    } else {
                        this.finalMessage += this.message[i]
                    }
                }, interval * i)
            }
        },

        async logout() {
            const token = localStorage.getItem('token')
            // axios.defaults.headers.common['Authorization'] = `Token ${store.state.token}`;

            if (!token) {
                console.log('Token not found')
                return
            }

            axios
                .post('token/logout/', {
                    headers: {
                        'Authorization': `Token ${token}`,
                    }
                })
                .then(response => {

                    this.$store.commit('removeToken')
                    localStorage.removeItem('token')
                    localStorage.setItem('auth_status', false)

                    delete axios.defaults.headers.common['Authorization']

                    this.isAuthenticated = false

                    this.$router.push('/user/log-in/')
                })
                .catch(error => {
                    console.log(error)

                    this.$store.commit('removeToken')
                    localStorage.removeItem('token')
                    localStorage.setItem('auth_status', false)

                    delete axios.defaults.headers.common['Authorization']

                    this.isAuthenticated = false

                    this.$router.push('/user/log-in/')
                })
        },

        getResult() {
            this.fetchSearchResults().then(() => {
                this.startAnimation()
                this.startPlaylistAntimation()
            })
        },

        async fetchSearchResults() {
            const searchBlock = document.getElementById('searchBlock')

            if (this.searchQuery) {
                searchBlock.classList.add('active')
            } else {
                searchBlock.classList.remove('active')
            }

            try {
                const response = await axios.get(`search/?query=${this.searchQuery}`)

                this.songs = response.data.songs
                this.playlists = response.data.playlists
                this.profiles = response.data.profiles

                this.startAnimation()
                this.startPlaylistAntimation()
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
        this.isAuthenticated = localStorage.getItem('auth_status') === 'true' ? true : false
        this.searchFieldAnimation()

        this.url = this.$store.getters.getBaseURL

        setInterval(this.searchFieldAnimation, 10000)
    }
}
</script>

<style lang="scss">
nav {
    position: sticky;
    z-index: 2;
    top: 0;

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 0 50px;
    width: 100%;
    height: 70px;
    background-color: antiquewhite;

    color: #000000;
    font-size: 16px;

}

nav div .navbar-brand a {
    color: #000000;
    font-size: 22px;
    font-family: "Nerko One", cursive;
    font-weight: bold;
    font-style: normal;

    margin-right: 30px;
}

nav div {
    display: flex;
    align-items: center;
}

nav div .navbar-menu ul,
nav .icons-menu ul,
nav .vertical-icons-menu ul {
    display: flex;
}

nav div .navbar-menu ul li,
nav div .vertical-navbar-menu ul li {
    color: #ffffff;
    position: relative;
    margin: 50px 10px;
}

nav div .navbar-menu ul li a,
nav div .vertical-navbar-menu ul li a,
nav div .navbar-menu ul li button,
nav div .vertical-navbar-menu ul li button {
    color: #000000;
}

nav div .navbar-menu ul li a::before,
nav div .verical-navbar-menu ul li a::before,
nav div .navbar-menu ul li button::before,
nav div .verical-navbar-menu ul li button::before {
    content: "";

    position: absolute;
    bottom: -5px;
    left: 50%;
    transform: translateX(-50%);

    height: 1.5px;
    width: 0;

    background-color: #000000;
    transition: all .3s ease-out;
}

nav div .navbar-menu ul li:hover a::before,
nav div .vertical-navbar-menu ul li:hover a::before,
nav div .navbar-menu ul li:hover button::before,
nav div .vertical-navbar-menu ul li:hover button::before {
    width: 100%;
}


form {
    display: flex;
    align-items: center;
    justify-content: center;
}


nav .search-form input[type="text"],
nav .vertical-search-form input[type="text"] {
    width: 260px;
    height: 40px;

    padding: 0 20px;

    color: #000000;
    border-radius: 10px 0 0 10px;
}

nav .search-form button,
nav .vertical-search-form button {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 40px;
    height: 40px;

    background-color: #ffffff;
    color: #000000;
    border-radius: 0 10px 10px 0;

    cursor: pointer;
}

nav .icons-menu ul li a svg,
nav .vertical-icons-menu ul li a svg {
    width: 20px;
    height: 20px;

    margin: 0 10px;
    color: #000000;
}

nav .vertical-menu-btn {
    display: none;
    z-index: 3;
}

@media (max-width: 1200px) {

    nav div .navbar-menu,
    nav .search-form,
    nav .icons-menu {
        display: none;
    }

    nav .vertical-menu-btn {
        display: block;
    }
}


nav .vertical-menu {
    position: fixed;
    top: 0;
    right: -100%;

    display: none;
    flex-direction: column;
    justify-content: space-between;

    padding: 80px 0 10px 0;

    min-width: 320px;
    max-width: 420px;

    height: 100%;

    background-color: antiquewhite;
    transition: all .3s ease-out;
}

nav .vertical-menu.active {
    display: flex;
    right: 0;
}

nav .vertical-menu-btn {
    position: relative;

    width: 25px;
    height: 18px;

    cursor: pointer;
}

nav .vertical-menu-btn span {
    position: absolute;

    width: 100%;
    height: 1.5px;

    background-color: #000000;
    transition: all .3s ease-out;
}

nav .vertical-menu-btn span:nth-child(2) {
    top: 50%;
    transform: translateY(-50%);
}

nav .vertical-menu-btn span:nth-child(3) {
    bottom: 1px;
}

nav .vertical-menu-btn.active span {
    top: 50%;
    transform: translateY(-50%);
}

nav .vertical-menu-btn.active span:nth-child(1) {
    transform: rotate(45deg);
}

nav .vertical-menu-btn.active span:nth-child(2) {
    display: none;
}

nav .vertical-menu-btn.active span:nth-child(3) {
    transform: rotate(-45deg);
}

div#searchBlock {
    position: absolute;
    overflow-x: hidden;
    top: 80px;
    left: 50%;
    transform: translateX(-50%);

    width: 800px;
    height: 500px;


    display: none;

    &.active {
        display: block;
    }

    .search-block-wrap {
        width: 800px;
        min-height: 500px;
        height: auto;
        padding: 10px 20px;

        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: center;

        background-color: antiquewhite;

        .card {
            display: flex;
            justify-content: space-between;
            width: 100%;
        }

        .profile-wrap {
            display: flex;
            flex-wrap: wrap;
            justify-content: start;
            width: 100%;

            .block:nth-child(1) {
                margin-left: 0px !important;
            }

            .block {
                display: flex;
                flex-direction: column;
                width: 90px;
                height: 90px;

                img {
                    width: 90px;
                    height: 90px;

                    border-radius: 50%;
                }

                a {
                    color: #0000EE;
                }
            }
        }

        .playlist-wrap {
            display: flex;
            justify-content: start;
            flex-wrap: wrap;
            width: 100%;

            .block:nth-child(1) {
                margin-left: 0px !important;
            }

            .block {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: space-between;
                width: 90px;
                min-height: 140px;
                max-height: 140px;
                margin-right: 10px;
                background-color: #fcf4ea;


                img {
                    width: 90px;
                    height: 90px;
                }

                .footer {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;

                    height: 30px;

                    .play {
                        a svg {
                            width: 20px;
                            height: 20px;
                        }
                    }

                    button {
                        transform: scale(1);
                    }
                }
            }
        }

    }
}

@media(max-width: 900px) {
    div#searchBlock {
        width: 500px;

        .search-block-wrap {
            width: 500px;

            .player {
                margin-left: 20px !important;
            }
        }
    }
}


@media(max-width: 600px) {
    div#searchBlock {
        width: 300px;

        .search-block-wrap {
            width: 300px;

            .card {
                padding: 10px 10px;
            }


            .info-btn,
            .count,
            .progress,
            .info img,
            .like span,
            .addToPlaylist {
                display: none;
            }

            .like {
                margin: 0 0 0 10px !important;
            }
        }
    }
}
</style>