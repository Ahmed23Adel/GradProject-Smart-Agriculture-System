<script setup>
import Calendar from 'primevue/calendar';
import { ref, onMounted, watch  } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';
import { formatDate } from '@/modules/Basic.ts';


const today = new Date(); // Create a new Date object for today's date
const date = ref(today);
const count = ref(0);
const percentageDiseased = ref(0);
const percentageDiseasedAfterMod = ref(0);
const mod_rate = ref(0);
const eb_per = ref(0);
const lb_per = ref(0);
const chartData = ref();
const chartOptions = ref();



const fetchRoundStatsAtDate = async () => {
    console.log(formatDate(date.value))
    const queryParams = {
        date_str: formatDate(date.value),
    };
    const requester = new HttpRequester('date_pics');
    const requester_data = await requester.callApi('GET', queryParams);
    count.value = requester_data.count;
    percentageDiseased.value = requester_data.percentage_diseased;
    percentageDiseasedAfterMod.value = requester_data.percentage_diseased_after_mod;
    mod_rate.value = requester_data.mod_rate;
    eb_per.value = requester_data.EB_per;
    lb_per.value = requester_data.LB_per;
};




const setChartData = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    
    return {
        labels: ['Early blight', 'Late bligh'],
        datasets: [
            {
                label: "% of disease type",
                backgroundColor: documentStyle.getPropertyValue('--gray-500'),
                borderColor: documentStyle.getPropertyValue('--gray-500'),
                data: [eb_per.value, lb_per.value]
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
        maintainAspectRatio: false,
        aspectRatio: 0.8,
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
                    color: textColorSecondary,
                    font: {
                        weight: 500
                    }
                },
                grid: {
                    display: false,
                    drawBorder: false
                }
            },
            y: {
                ticks: {
                    color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder,
                    drawBorder: false
                }
            }
        }
    };
}

onMounted(async () => {
    await fetchRoundStatsAtDate();
    chartData.value = setChartData();
    chartOptions.value = setChartOptions();
    
});

watch(date, (newDate) => {
    const formattedDate = formatDate(newDate);
    fetchRoundStatsAtDate(formattedDate);
});
</script>
<template>
    <div class="row" style="padding:30px">
        <div class="col-6">
            <h1 class="h3">At specific date:</h1>
        </div>
        <div class="col-6">
            <FloatLabel>
                <Calendar v-model="date" inputId="birth_date" />
                <label for="birth_date">Date</label>
            </FloatLabel>
        </div>

    </div>
    <div class="row">
        <div class="col-xs-12 col-sm-12 col-md-12 col-xl-8">

            <div class="row">
                <div class="row">
                    <div class="col-3">
                        <div class="card" style="width: 12rem; background-color:#F4EDCC; border-radius: 20%;">
                            <img src='/src/assets/images/stats/stats1.png' class="card-img-top card-img" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">Count</h5>
                                <p class="card-text">{{ count }} images</p>
                                <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
                            </div>
                        </div>
                    </div>
                    <div class="col-3">
                        <div class="card" style="width: 12rem; background-color:#5F5D9C; border-radius: 20%;">
                            <img src='/src/assets/images/stats/stats2.png' class="card-img-top card-img" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">% diseased</h5>
                                <p class="card-text">{{ percentageDiseased }}%</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-3">
                        <div class="card" style="width: 12rem; background-color:#6196A6; border-radius: 20%;">
                            <img src='/src/assets/images/stats/modify.png' class="card-img-top card-img" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">% diseased after modification</h5>
                                <p class="card-text">{{ percentageDiseasedAfterMod }}%</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-3">
                        <div class="card" style="width: 12rem; background-color:#A4CE95; border-radius: 20%;">
                            <img src='/src/assets/images/stats/percentage.png' class="card-img-top card-img" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">Modification rate</h5>
                                <p class="card-text">{{ mod_rate }}%</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-4 disease-percen">
            <Chart type="bar" :data="chartData" :options="chartOptions" class="h-30rem" />
        </div>
    </div>

</template>

<style scoped>
.card-img {
    max-width: 70px;
    left: 0;
    height: auto;
    margin: 20px;
}

.disease-percen {
    /* margin-top:100px; */
    padding: 30px;
    background-color: #A4CE95;
    border-radius: 20%;
    /* padding-right:50px; */
    /* margin:20px; */
}
</style>