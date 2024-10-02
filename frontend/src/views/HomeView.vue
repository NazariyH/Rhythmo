<template>
  <div class="home">
    <div class="section">
      <div class="content-section">
        <div class="profile-wrap">
          <span v-on:click="back">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
              class="bi bi-arrow-left-circle-fill" viewBox="0 0 16 16">
              <path
                d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0m3.5 7.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z" />
            </svg>
          </span>

          <div class="sub-wrap">
            <div class="slider">
              <div class="block" v-for="profile in profiles" :key="profile.user">
                <img :src="`${url}/${profile.profileImage}`" alt="profile">

                <router-link :to="{ name: 'profile', params: { id: profile.user } }">
                  {{ profile.fullName.slice(0, 5) + '..' }}
                </router-link>
              </div>
            </div>
          </div>

          <span v-on:click="next">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
              class="bi bi-arrow-right-circle-fill" viewBox="0 0 16 16">
              <path
                d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0M4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5z" />
            </svg>
          </span>
        </div>

        <div class="content-block">
          <Song v-for="song in songs" :song="song" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import Song from '@/components/Song'
import Playlist from '@/components/Playlist'

export default {
  name: 'HomeView',
  components: {
    Song,
    Playlist,
  },
  data() {
    return {
      songs: null,
      profiles: null,
      url: '',
      currentX: 0,
    }
  },
  methods: {
    async fetchRecomendedData() {
      try {
        const response = await axios.get('recomendation/')

        this.songs = response.data.songs
        this.profiles = response.data.profiles
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

    next() {
      const sub_wrap = document.querySelector('.slider')

      if (document.body.offsetWidth < 680) {
        if (this.currentX == (this.profiles.length - 2) * -140) {
          this.currentX = 0
        } else {
          this.currentX -= 140
        }
      } else if (document.body.offsetWidth > 680 && document.body.offsetWidth < 1000) {
        if (this.currentX == (this.profiles.length - 4) * -140) {
          this.currentX = 0
        } else {
          this.currentX -= 140
        }
      } else if (document.body.offsetWidth > 1000 && document.body.offsetWidth < 1400) {
        if (this.currentX == (this.profiles.length - 6) * -140) {
          this.currentX = 0
        } else {
          this.currentX -= 140
        }
      } else {
        if (this.currentX == (this.profiles.length - 8) * -140) {
          this.currentX = 0
        } else {
          this.currentX -= 140
        }
      }

      sub_wrap.style.transform = `translateX(${this.currentX}px)`
    },

    back() {
      console.log(document.body.offsetWidth)
      const sub_wrap = document.querySelector('.slider')

      this.currentX += 140
      console.log(this.currentX)

      if (this.currentX > 0) {
        if (document.body.offsetWidth < 680) {
          this.currentX = (this.profiles.length - 2) * -140;
        } else if (document.body.offsetWidth > 1000 && document.body.offsetWidth < 1400) {
          this.currentX = (this.profiles.length - 6) * -140;
        } else if (document.body.offsetWidth > 680 && document.body.offsetWidth < 1000) {
          this.currentX = (this.profiles.length - 4) * -140;
        } else {
          this.currentX = (this.profiles.length - 8) * -140;
        }
      }


      sub_wrap.style.transform = `translateX(${this.currentX}px)`
    }
  },
  mounted() {
    this.url = this.$store.getters.getBaseURL
    this.fetchRecomendedData().then(() => {
      this.startAnimation()
    })
  }
}
</script>


<style lang="scss">
@media(max-width: 680px) {
  .sub-wrap {
    width: 280px !important;
  }
}

@media(min-width: 1000px) {
  .sub-wrap {
    width: 840px !important;
  }
}

@media(min-width: 1400px) {
  .sub-wrap {
    width: 1120px !important;
  }
}

.profile-wrap {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;

  padding: 0 30px !important;

  span,
  span svg {
    width: 35px;
    height: 35px;
  }

  .sub-wrap {
    width: 560px;
    overflow-x: hidden;

    .slider {
      display: flex;
      transition: all .5s ease-in-out;

      .block {
        display: flex;
        flex-direction: column;
        padding: 0 10px !important;

        background-color: inherit !important;
        margin: 0 !important;

        img {
          width: 120px;
          height: 120px;

          border-radius: 50%;
        }

        a {
          color: #0000EE;
        }
      }
    }
  }
}
</style>