<script setup>
import { ref, onMounted, watch } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';
import { formatDate } from '@/modules/Basic.ts';

const today = new Date(); // Create a new Date object for today's date
const atDate = ref(today)
const diseases = ref()
const percentages = ref()
const chartData = ref();
const chartOptions = ref();
const isShowNoData = ref(false)
const isShowLoading = ref(true)

async function fetchDiseasePercentages() {
    isShowLoading.value = true;
    isShowNoData.value = false;
    const requester = new HttpRequester('get-blight-images-percentage');
    const queryParams = {
        date: formatDate(atDate.value)
    };
    const requester_data = await requester.callApi('GET', queryParams);
    diseases.value = requester_data.diseases;
    percentages.value = requester_data.percentages;
    if (percentages.value.every(value => value === 0)){
        isShowNoData.value = true;
    }
    isShowLoading.value = false;
}

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

onMounted(async () => {
    await fetchDiseasePercentages();
    chartData.value = setChartData();
    chartOptions.value = setChartOptions();
    
});

watch(atDate, async (newDate) => {
    const formattedDate = formatDate(newDate);
    await fetchDiseasePercentages(formattedDate);
    chartData.value = setChartData();
    chartOptions.value = setChartOptions();
});




</script>
<template>
    <div class="row">
        <h1 class="h3">At date:</h1>
    </div>
    <div class="row">
        <div class="col-4">
            <div class="card flex justify-content-center" style="margin:20px">
                <Calendar v-model="atDate" />
            </div>
        </div>
        <div class="col-4">
            <div class="row justify-content-center" v-if="isShowLoading">
                <div class="col-12 text-center">
                    <ProgressSpinner />
                </div>
            </div>
        </div>
       
    </div>
    <div v-if="isShowNoData">
        <Message severity="warn">No data for this date. Please try another date</Message>
    </div>
    
    <div class="row">
        <div class="col-12">
            <div class="chart-parent-center">
                <div clas="grid-content ep-bg-purple chart-parent">
                    <div class="card flex justify-content-center chart-parent">
                        <Chart type="pie" :data="chartData" :options="chartOptions" class="w-full md:w-30rem" />
                    </div>
                </div>
            </div>>

        </div>
    </div>


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