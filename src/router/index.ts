import LoginView from "../views/LoginView.vue"
import NotFound from "../views/NotFound.vue"
import StatsView from "../views/StatsView.vue"
import Summary from   '../views/Summary.vue'
import Reports from  '../views/Reports.vue'
import Treatment from   '../views/Treatment.vue'
import DiseaseDefaultTreatment from   '../views/DiseaseDefaultTreatment.vue'
import RegisterNewUser from   '../views/RegisterNewUser.vue'
import ownerReport from "@/views/ownerReport.vue"
import ZonesMapping from "@/views/ZonesMapping.vue"

import { createRouter, createWebHistory } from "vue-router"

const router = createRouter({
    history:createWebHistory(import.meta.env.BASE_URL),
    routes:[    
        {
            path:"/",
            name:"mainpage",
            component: LoginView
        },
        {
            path:"/login",
            name:"login",
            component: LoginView
        },
        {
            path:"/treatment",
            name:"treatment",
            component: Treatment
        },
        {
            path:"/treatment/disease-default-treatment/:id",
            name:"DiseaseTreatmentDefault",
            component: DiseaseDefaultTreatment
        },
        {
            path:"/stats",
            name:"stats",
            component: StatsView
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
        },        
        {
            path:"/register",
            name:"register",
            component: RegisterNewUser
        
        },
        {
            path:"/ownerReport",
            name:"ownerReport",
            component: ownerReport
        },
        {
            path:"/zonesMapping",
            name:"zonesMapping",
            component: ZonesMapping
        }, 
        {
            path:"/:catchall(.*)*",
            name:"Not found",
            component: NotFound
        },

    ]
})

export default router