<script setup>
import { ref, onMounted, watch } from "vue";
import { HttpRequester } from './nets'; // Adjust the file path as necessary
const bearer = 'hi';

const today = new Date(); // Create a new Date object for today's date
const atDate = ref(today)
const diseases = ref()
const percentages = ref()

async function fetchDiseasePercentages() {
    const requester = new HttpRequester('http://127.0.0.1:8000/get_disease_statistics', bearer);
    const queryParams = {
        date: atDate.value
    };
    console.log("queryParams", queryParams)
    const requester_data = await requester.callApi(queryParams);
    diseases.value = requester_data.diseases;
    percentages.value = requester_data.percentages;
}

onMounted(async () => {
    await fetchDiseasePercentages();
    chartData.value = setChartData();
    chartOptions.value = setChartOptions();
    
});

function formatDate(date) {
    const month = date.getMonth() + 1; // Months are 0-based, so add 1
    const day = date.getDate();
    const year = date.getFullYear();
    // Pad month and  with leading zeros if necessary
    const paddedMonth = month.toString().padStart(2, '0');
    const paddedDay = day.toString().padStart(2, '0');
    // Return the formatted date as a string
    return `${paddedMonth}/${paddedDay}/${year}`;
}

watch(atDate, (newDate) => {
    const formattedDate = formatDate(newDate);
    fetchDiseasePercentages(formattedDate);
});

const chartData = ref();
const chartOptions = ref();

const setChartData = () => {
    const documentStyle = getComputedStyle(document.body);

    return {
        labels: diseases.value,
        datasets: [
            {
                data: percentages.value,
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
                <!-- <p class="pre-date" style="margin:20px"> At date: </p> -->
                <h1 class="h3">At date:</h1>
                <div class="card flex justify-content-center" style="margin:20px">
                    <Calendar v-model="atDate" />
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
    height: 100%; 
    background-color: #A4CE95;
}
</style>