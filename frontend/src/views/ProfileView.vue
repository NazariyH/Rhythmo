<template>
  <div class="section">
    <ProfileInfo :profileImage="profileImage" :username="username" :age="age" :bio="bio" :gender="gender" :followers="followers"/>

    <div class="list-of-playlists">
      <!-- Add playlist rendering logic here -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProfileInfo from '@/components/ProfileInfo.vue';

export default {
  name: 'Profile',
  data() {
    return {
      username: '',
      age: null,
      bio: '',
      gender: '',
      followers: 0,
      profileImage: ''
    };
  },
  components: {
    ProfileInfo,
  },
  methods: {
    async fetchData() {
      const token = localStorage.getItem('token')

      if (token) {
        axios.defaults.headers.common['Authorization'] = 'Token ' + token

        try {
          const response = await axios.get('user/profile/')
          const profileData = response.data.profile

          this.username = profileData.fullName
          this.age = profileData.age
          this.bio = profileData.bio
          this.gender = profileData.gender
          this.followers = profileData.followers.length
          this.profileImage = `http://localhost:8000${profileData.profileImage}`

        } catch (error) {
          console.error('Error fetching profile:', error.response ? error.response.data : error.message)
        }
      } else {
        console.error('No authentication token found.')
      }
    }
  },
  mounted() {
    this.fetchData()
  }
}
</script>

<style>
hr {
  border: 0.5px solid #c6c6c6;
  width: 100%;
  margin: 30px 0;
}
</style>
