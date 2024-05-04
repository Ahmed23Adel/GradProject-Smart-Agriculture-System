<script setup>
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import { ref, onMounted } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';


//The four cards
const count = ref(0);
const percentageDiseased = ref(0);
const percentageDiseasedAfterMod = ref(0);
const modRate = ref(0);
// Graph for months and percentage
const mons = ref([]);
const EB = ref([]);
const LB = ref([]);
const chartData = ref();
const chartOptions = ref();


const fetchTodayStats = async () => {
    const requester = new HttpRequester('today_pics');
    const requester_data = await requester.callApi('GET');
    count.value = requester_data.count;
    percentageDiseased.value = requester_data.percentage_diseased;
    percentageDiseasedAfterMod.value = requester_data.percentage_diseased_after_mod;
    modRate.value = requester_data.mod_rate;
};


const fetchMonsPercentages = async () => {
    const requester = new HttpRequester('disease_mons_percentage');
    const requester_data = await requester.callApi('GET');
    mons.value = requester_data.mons;
    EB.value = requester_data.EB;
    LB.value = requester_data.LB;
};


const setChartData = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    return {
        labels: mons.value,
        
        datasets: [
            {
                label: 'Early blight',
                data: EB.value,
                fill: false,
                borderColor: documentStyle.getPropertyValue('--cyan-500'),
                tension: 0.4
            },
            {
                label: 'Late blight',
                data: LB.value,
                fill: false,
                borderColor: documentStyle.getPropertyValue('--gray-500'),
                tension: 0.4
            }
        ]
    };
};

onMounted(async () => {
    await fetchMonsPercentages();
    fetchTodayStats();
    chartData.value = setChartData();
    chartOptions.value = setChartOptions();
    
});


const setChartOptions = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--text-color');
    const textColorSecondary = documentStyle.getPropertyValue('--text-color-secondary');
    const surfaceBorder = documentStyle.getPropertyValue('--surface-border');

    return {
        maintainAspectRatio: false,
        aspectRatio: 0.6,
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

</script>


<template>
    <div class="row">
        <div class="col-xs-12 col-sm-12 col-md-12 col-xl-8">
            <div class="row" style="padding:30px">
                <div class="col-8">
                    <h1 class="h3">Today's Pictures</h1>

                </div>
                <div class="col-4">
                    <button type="button" class="btn btn-primary">Go to Today's section</button>
                </div>
            </div>
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
                                <p class="card-text">{{ modRate }}%</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-4 disease-percen">
                <Chart type="line" :data="chartData" :options="chartOptions" class="h-30rem" />
        </div>
    </div>
</template>


<style scoped>
.card-img{
    max-width: 70px;
    left: 0;
    height: auto;
    margin:20px;
}
.disease-percen{
    margin-top:100px;
    padding:30px;
    background-color:#A4CE95;
    border-radius:20%;
    padding-right:50px;
    /* margin:20px; */
}
</style>