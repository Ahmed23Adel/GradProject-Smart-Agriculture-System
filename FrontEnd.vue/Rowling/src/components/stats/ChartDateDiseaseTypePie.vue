<script setup>
import { ref, onMounted } from "vue";

onMounted(() => {
    chartData.value = setChartData();
    chartOptions.value = setChartOptions();
});

const chartData = ref();
const chartOptions = ref();

const setChartData = () => {
    const documentStyle = getComputedStyle(document.body);

    return {
        labels: ['Early blight', 'LateBlight', 'others'],
        datasets: [
            {
                data: [540, 325, 702],
                backgroundColor: [documentStyle.getPropertyValue('--cyan-500'), documentStyle.getPropertyValue('--orange-500'), documentStyle.getPropertyValue('--gray-500')],
                hoverBackgroundColor: [documentStyle.getPropertyValue('--cyan-400'), documentStyle.getPropertyValue('--orange-400'), documentStyle.getPropertyValue('--gray-400')]
            }
        ]
    };
};

const setChartOptions = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--text-color');

    return {
        plugins: {
            legend: {
                labels: {
                    usePointStyle: true,
                    color: textColor
                }
            }
        }
    };
};
</script>
<template>
    <el-row>
        <el-col :span="8" :xs="24" :sm="24" :md="24" :lg="8" :xl="8">
            <div class="grid-content ep-bg-purple">
                <p class="pre-date" style="margin:20px"> At date: </p>
                <div class="card flex justify-content-center" style="margin:20px">
                    <Calendar v-model="fromDate" />
                </div>
            </div>
        </el-col>
    </el-row>

    <el-row>
        <el-col :span="24">
            <div class="chart-parent-center">
                <div clas="grid-content ep-bg-purple chart-parent">
                    <div class="card flex justify-content-center chart-parent">
                        <Chart type="pie" :data="chartData" :options="chartOptions" class="w-full md:w-30rem" />
                    </div>
                </div>
            </div>>

        </el-col>
    </el-row>


</template>

<style scoped>
.chart-parent {
    width: 500px; /* Adjust width as needed */
    height: 500px; /* Adjust height as needed */
}

.chart-parent-center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%; /* Ensure the container fills the height of its parent */
}
</style>