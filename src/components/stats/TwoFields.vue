<script setup>
    import {defineProps} from "vue"

    const { firstField, secondField } = defineProps(['firstField','secondField']);
    console.log("firstField: " + firstField)
    console.log("secondField: " + secondField)
</script>
<template>
    <el-row>
        <el-col :span="11">
            <div class="grid-content ep-bg-purple">
                <p class="stat-item">{{ firstField }}</p>
            </div>
        </el-col>
        <el-col :span="11">
            <div class="grid-content ep-bg-purple">
                <p class="stat-item">{{ secondField }}</p>
            </div>
        </el-col>
    </el-row>
    <!-- <hr class="bet-items-sep">  -->
</template>

<style scoped>
    .stat-item{
    color: #5F5D9C;
    font-size: x-large;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 20px;
    font-weight: bold;
}

.bet-items-sep{
    width: 100wh; 
    border: none;
    border-top: 2px solid #000; /* Horizontal line style */
    margin-left: 40%;
    margin-right: 40%;
}

</style>