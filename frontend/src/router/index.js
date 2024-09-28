import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/authentication/LoginView.vue'
import SignupView from '@/views/authentication/SignupView.vue'
import OwnProfileView from '@/views/OwnProfileView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProfileEditView from '@/views/ProfileEditView.vue'
import AddSongView from '@/views/AddSongView.vue'
import AddPlaylistView from '@/views/AddPlaylist.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/user/log-in/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/user/sign-up/',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/user/profile/',
    name: 'user-profile',
    component: OwnProfileView
  },
  {
    path: '/user/profile/:id/',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/user/profile/edit/',
    name: 'profile-edit',
    component: ProfileEditView
  },
  {
    path: '/player/add-song/',
    name: 'add-song',
    component: AddSongView
  },
  {
    path: '/player/add-playlist/',
    name: 'add-playlist',
    component: AddPlaylistView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
