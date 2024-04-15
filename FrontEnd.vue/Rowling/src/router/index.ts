import LoginView from "../views/LoginView.vue"
import NotFound from "../views/NotFound.vue"
import StatsView from "../views/StatsView.vue"
import Summary from   '../views/Summary.vue'
import Reports from  '../views/Reports.vue'
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
            path:"/stats",
            name:"stats",
            component: StatsView
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
        },
        {
            path:"/reports",
            name:"reports",
            component: Reports
        }

    ]
})

export default router