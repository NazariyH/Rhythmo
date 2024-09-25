<template>
  <div class="home">

  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'HomeView',
  components: {
  },
  methods: {
    async fetchSpecificProfile() {
      const token = localStorage.getItem('token')

      if (!token) {
        console.log('Token not found')
        return
      }

      try {
        const response = await axios.post('user/profile/1/', null, {
          headers: {
            Authorization: `Token ${token}`
          }
        })
      } catch (error) {
        console.log(error)
      }
    }
  },
  mounted() {
    // this.fetchSpecificProfile()
  }
}
</script>
