import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/authentication/LoginView.vue'
import SignupView from '@/views/authentication/SignupView.vue'
import OwnProfileView from '@/views/OwnProfileView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProfileEditView from '@/views/ProfileEditView.vue'
import AddSongView from '@/views/AddSongView.vue'
import AddPlaylistView from '@/views/AddPlaylist.vue'
import PlaylistDetailView from '@/views/PlaylistDetailView.vue'
import EditPlaylistView from '@/views/EditPlaylistView.vue'
import Payment from '@/views/Payment.vue'

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
    name: 'current-profile',
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
    path: '/playlist/:id/edit/',
    name: 'edit-playlist',
    component: EditPlaylistView,
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
  },
  {
    path: '/player/playlist/:id/detail/',
    name: 'playlist-detail',
    component: PlaylistDetailView
  },
  {
    path: '/payment/',
    name: 'payment',
    component: Payment
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
