import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import 'primevue/resources/themes/lara-dark-teal/theme.css'
import PrimeVue from 'primevue/config';
import InputText from 'primevue/inputtext'
import FloatLabel from 'primevue/floatlabel';
import Password from 'primevue/password';

import Message from 'primevue/message';

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

const app = createApp(App, { ripple: true });

app.use(router)
app.use(ElementPlus)
app.use(PrimeVue);
app.component('InputText', InputText)
app.component('FloatLabel', FloatLabel)
app.component('Password', Password)
app.component('Message', Message)

app.mount('#app')