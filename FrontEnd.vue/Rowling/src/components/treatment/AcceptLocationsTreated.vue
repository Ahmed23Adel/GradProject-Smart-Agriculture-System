<script setup>
import { ref, onMounted, watch } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';
import { UserType } from '@/modules/Basic.ts';
import { fetchAllLocations } from '@/modules/CommonRequests.ts';

const isOwner = ref(false);
const locations = ref([])
const selectedLocation = ref();
const images = ref();


async function fetchLocationHistory() {
    const requester = new HttpRequester('location-history',);
    const queryParams = {
        location: selectedLocation.value.name,
        from_date: "01/01/0001",
        to_date: "01/01/0001",
    };
    const requester_data = await requester.callApi("GET",queryParams);
    images.value = requester_data.allHistory;
}

async function accpetTreated(){
    const requester = new HttpRequester('accept-treated');
    const queryParams = {
        location: selectedLocation.value.name,
    };
    console.log("selectedLocation.value", queryParams)
    await requester.callApi("PUT",queryParams);
}


watch(selectedLocation, async (newSelectedLocation, oldSelectedLocation) => {
    await fetchLocationHistory();
});


onMounted(async () => {
    await fetchAllLocations(locations, selectedLocation);
    fetchLocationHistory()
    isOwner.value = UserType.getInstance().getUserType();
});


</script>

<template>
    <h1 class="h3">Accept these locations are finished</h1>
    <h1 class="h6">These locations need your approval: </h1>

    <el-row>
        <el-col :span="8" :xs="24" :sm="24" :md="24" :lg="8" :xl="8">
            <div class="grid-content ep-bg-purple">
                <p class="pre-date" style="margin:20px"> Location </p>
                <div class="card flex justify-content-center" style="margin:20px">
                    <CascadeSelect v-model="selectedLocation" :options="locations" optionLabel="name"
                        optionGroupLabel="name" :optionGroupChildren="['subLocations']" style="min-width: 14rem"
                        placeholder="Select a Location" />
                </div>
            </div>
        </el-col>
    </el-row>

    <div class="row graph-parent">
        <div class="col-6 graph-parent">
            <div class="grid-content ep-bg-purple graph-image-parent">
                <div class="card">
                    <Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5"
                        containerStyle="max-width: 640px">
                        <template #item="slotProps">
                            <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt"
                                style="width: 100%; display: block" />
                        </template>
                        <template #thumbnail="slotProps">
                            <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt"
                                style="display: block" />
                        </template>
                        <template #caption="slotProps">
                            <div class="text-xl mb-2 font-bold">{{ slotProps.item.title }}</div>
                            <p class="text-white">{{ slotProps.item.alt }}</p>
                        </template>
                    </Galleria>
                </div>
            </div>
        </div>
        <div class="col-6">
            <div class="submit-parent">
                <div class="card flex justify-content-center submit-sub-parent">
                    <Button label="Accept treated" icon="pi pi-check" iconPos="right" class="submit-button" @click="accpetTreated" :disabled="isOwner"/>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.graph-parent {
    background-color: var(--primary);
}

.submit-parent {
    display: flex;
    justify-content: center;
    /* Center horizontally */
    align-items: center;
    /* Center vertically */
    margin-top: 30px;
    background-color: var(--primary);
}

.submit-button {
    border-radius: 20px;
}

.submit-sub-parent {
    background-color: var(--primary);
    border: none;
}
</style>