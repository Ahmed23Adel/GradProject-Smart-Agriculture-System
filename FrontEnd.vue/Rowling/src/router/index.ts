import LoginView from "../views/LoginView.vue"
import NotFound from "../views/NotFound.vue"
import Summary from '../views/Summary.vue'

import { createRouter, createWebHistory } from "vue-router"

const router = createRouter({
    history:createWebHistory(import.meta.env.BASE_URL),
    routes:[    
        {
            path:"/login",
            name:"login",
            component: LoginView
        },
        {
            path:"/:catchall(.*)*",
            name:"Not found",
            component: NotFound
        },
        {
            path:"/summary",
            name:"summary",
            component: Summary
        }
    ]
})

export default router