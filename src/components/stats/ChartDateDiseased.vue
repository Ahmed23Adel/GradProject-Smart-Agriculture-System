<script setup>
import { ref, onMounted, watch } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';
import { fetchAllLocations } from '@/modules/CommonRequests.ts';


const dates = ref();
const percentages = ref();
const chartData = ref();
const chartOptions = ref();
const locations = ref([])
const selectedLocation = ref();

async function fetchDatesDiseases() {
    console.log("fetchDatesDiseases")
    const requester = new HttpRequester('get-date-per-diseased-plants');
    const queryParams = {
        location: selectedLocation.value.name,
    };
    console.log("queryParamssss", queryParams)
    const requester_data = await requester.callApi('GET', queryParams);
    console.log("requester_datarequester_data", requester_data)
    dates.value = requester_data.dates;
    percentages.value = requester_data.percentages;
}



const setChartData = () => {
    const constantColorValue = 'rgba(164, 206, 149, 1)';
    const colorsArray = new Array(percentages.length).fill(constantColorValue);

    const constantBorderValue = 'rgb(139, 92, 246)';
    const bordersArray = new Array(percentages.length).fill(constantBorderValue);
    return {
        labels: dates.value,
        datasets: [
            {
                label: 'Percentage of diseased plants',
                data: percentages.value,
                backgroundColor: colorsArray,
                borderColor: bordersArray,
                borderWidth: 1
            }
        ]
    };
};
const setChartOptions = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--text-color');
    const textColorSecondary = documentStyle.getPropertyValue('--text-color-secondary');
    const surfaceBorder = documentStyle.getPropertyValue('--surface-border');

    return {
        plugins: {
            legend: {
                labels: {
                    color: textColor
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder
                }
            },
            y: {
                beginAtZero: true,
                ticks: {
                    color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder
                }
            }
        }
    };
}

watch(selectedLocation, async (newSelectedLocation, oldSelectedLocation) => {
    await fetchDatesDiseases();
    chartData.value = setChartData();
    chartOptions.value = setChartOptions();
});

onMounted(async () => {
    console.log("mounting")
    await fetchAllLocations(locations, selectedLocation);
    selectedLocation.value = locations.value[0];
    
});
</script>
<template>
    <div class="row">
        <div clas="col-4">
            <div class="grid-content ep-bg-purple">
                <h1 class="pre-date" style="margin:20px"> Location </h1>
                <div class="card flex justify-content-center" style="margin:20px">
                    <CascadeSelect v-model="selectedLocation" :options="locations" optionLabel="name"
                        optionGroupLabel="name" :optionGroupChildren="['subLocations']" style="min-width: 14rem"
                        placeholder="Select a Location" />
                </div>
            </div>
        </div>
    </div>
    <div class="label-container">
        Percentage of Diseased Plants Over Time
    </div> 
    <div class=row>
        <div class="col-12">
            <div class="chart-parent-center">
                <div clas="grid-content ep-bg-purple chart-parent">
                    <div class="card flex justify-content-center chart-parent">
                        <Chart type="bar" :data="chartData" :options="chartOptions" />
                    </div>
                </div>
            </div>>

        </div>
    </div>

</template>

<style scoped>
.chart-parent {
    width: 500px;
    height: 500px;
    background-color: var(--primary);
}

.chart-parent-center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;

}

.label-container {
    font-size: 1.2rem; 
    font-weight: bold;
    color: #333; 
    text-align: center; 
    margin-bottom: 1rem; 
    padding: 0.5rem; 
}

</style>