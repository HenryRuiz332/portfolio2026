import { createApp } from 'vue'
import { createPinia } from 'pinia'

// Base Styles
import './style.css'

// Portfolio Assets CSS
import './assets/css/bootstrap.min.css'
import './assets/css/open-iconic-bootstrap.min.css'
import './assets/css/animate.css'
import './assets/css/owl.carousel.min.css'
import './assets/css/owl.theme.default.min.css'
import './assets/css/magnific-popup.css'
import './assets/css/aos.css'
import './assets/css/ionicons.min.css'
import './assets/css/flaticon.css'
import './assets/css/icomoon.css'
import './assets/css/style.css'

import App from './App.vue'
import router from './router'

import AOS from 'aos'
import 'aos/dist/aos.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')

// Initialize AOS
AOS.init({
    duration: 800,
    easing: 'slide'
})
