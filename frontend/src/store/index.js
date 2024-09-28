import { createStore } from 'vuex'

export default createStore({
    state: {
        token: '',
        isAuthenticated: false,
        baseURL: 'http://192.168.116.193:8000/',
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('token')) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
            } else {
                state.token = ''
                state.isAuthenticated = false
            }
        },
        setToken(state, token) {
            state.token = token
            state.isAuthenticated = true // Set to true when token is received
        },
        removeToken(state) {
            state.token = ''
            state.isAuthenticated = false
        }
    },
    getters: {
        getBaseURL: state => state.baseURL,
    },
    actions: {},
    modules: {},
})
