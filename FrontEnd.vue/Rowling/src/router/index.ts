import LoginView from "../views/LoginView.vue"
import { createRouter, createWebHistory } from "vue-router"
import NotFound from "../views/NotFound.vue"
import StatsView from "../views/StatsView.vue"

const router = createRouter({
    history:createWebHistory(import.meta.env.BASE_URL),
    routes:[    
        {
            path:"/login",
            name:"login",
            component: LoginView
        },
        {
            path:"/stats",
            name:"stats",
            component: StatsView
        },
        {
            path:"/:catchall(.*)*",
            name:"Not found",
            component: NotFound
        }
    ]
})

export default router