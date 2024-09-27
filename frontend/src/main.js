import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';

axios.defaults.baseURL = 'http://192.168.116.137:8000/api/v1/';

const app = createApp(App);

// Use Vue Router, Vuex, and axios
app.use(router);
app.use(store);

// other configurations


// Optionally, you can globally provide axios if needed
app.config.globalProperties.$axios = axios;

// Mount the app
app.mount('#app');
