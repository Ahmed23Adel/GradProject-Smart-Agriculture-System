<script setup>
import Sidebar from "../components/Sidebar.vue";
import { ref, onMounted, watch } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';
import { UserType } from '@/modules/Basic.ts';
import viewAndChangeDefaultTreatment from "../components/settings/viewAndChangeDefaultTreatment.vue"
import addNewSavedTreatment from "../components/settings/addNewSavedTreatment.vue"
import movingCar from "../components/settings/movingCar.vue"
 
</script>
<template>
    <div class="page-container">
        <Sidebar class="sidebar" :selected="7" />
        <div class="main-container">
            <viewAndChangeDefaultTreatment/>
            <hr class="header-line">
            <addNewSavedTreatment/>
            <hr class="header-line">
            <movingCar/>
        </div>
    </div>
</template>
<style lang="scss" scoped>
.page-container {
    background-color: var(--primary);
    display: grid;
    position: relative;
    grid-template-columns: 150px 1fr;
}


.sidebar {
    position: sticky;
    top: 0;
}

.math-intro-container {
    // transform: translateY(-50%);
    top: 0;
}

.box {
    border: 2px solid;
    border-radius: 50px;
    /* Rounded corners */
    margin: 30px;
    padding: 30px;
    border-width: 20px;
    cursor: pointer;
}

.selected .box {
    border-color: green;
}

table {
    max-width: 100%;
    width: 100%;
    font-family: 'Arial';
    margin: 25px auto;
    border-collapse: collapse;
    border: 1px solid #eee;
    border-bottom: 2px solid #00cccc;
    box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.10),
        0px 10px 20px rgba(0, 0, 0, 0.05),
        0px 20px 20px rgba(0, 0, 0, 0.05),
        0px 30px 20px rgba(0, 0, 0, 0.05);

    tr {
        &:hover {
            background: #f4f4f4;

            td {
                color: #555;
            }
        }
    }

    th,
    td {
        color: #424242;
        border: 1px solid #eee;
        padding: 12px 35px;
        border-collapse: collapse;
    }

    th {
        background: #00cccc;
        color: #fff;
        text-transform: uppercase;
        font-size: 12px;

        &.last {
            border-right: none;
        }
    }
}

.ios-change {
    color: blue;
    /* Set text color to blue */
    cursor: pointer;
    /* Change cursor to pointer */
    text-decoration: underline;
    /* Add underline */
}

.align-items-center {
    display: flex;
    align-items: center;
    /* Vertically center the items */
}

.button-74 {
    background-color: #fbeee0;
    border: 2px solid #422800;
    border-radius: 30px;
    box-shadow: #422800 4px 4px 0 0;
    color: #422800;
    cursor: pointer;
    display: inline-block;
    font-weight: 600;
    font-size: 18px;
    padding: 0 18px;
    line-height: 50px;
    text-align: center;
    text-decoration: none;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
}

.button-74:hover {
    background-color: #fff;
}

.button-74:active {
    box-shadow: #422800 2px 2px 0 0;
    transform: translate(2px, 2px);
}

@media (min-width: 768px) {
    .button-74 {
        min-width: 120px;
        padding: 0 25px;
    }
}
</style>