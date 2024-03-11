<script setup>
import TwoFields from '@/components/stats/TwoFields.vue';

</script>
<template>

    <el-row>
        <el-col :span="22">
            <div class="grid-content ep-bg-purple">
                <h2 class="sub-header-gen-stats"></h2>
                <h1 class="h3">At specific date:</h1>
            </div>
        </el-col>
    </el-row>

    <el-row>
        <el-col :span="12" :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
            <div class="grid-content ep-bg-purple date-container">
                <p class="pre-date" style="margin:20px"> At: </p>

            </div>
        </el-col>
        <el-col :span="12" :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
            <div class="grid-content ep-bg-purple date-container">
                <div class="card flex justify-content-center" style="margin:20px">
                    <Calendar v-model="atDate" />
                </div>
            </div>

        </el-col>
    </el-row>
    <TwoFields :firstField="'Percentage of diseased plants according to the model'" :secondField="'30%'"/>
    <TwoFields :firstField="'Percentage of diseased plants after modification by an expert'" :secondField="'32%'"/>
                
</template>

<style scoped>
.sub-header-gen-stats {
    color: black;
    left: 0%;
}

.date-container {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin:20px
}

.pre-date{
    font-size: 28px;
}
</style>
