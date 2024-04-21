<script setup>
import { ref, onMounted, defineProps } from "vue";
import { PhotoService } from '@/services/PhotoService.ts';

defineProps(["location"])
console.log("location Graph", location)
onMounted(() => {
    PhotoService.getImages().then((data) => (images.value = data));
});

const images = ref();
const responsiveOptions = ref([
    {
        breakpoint: '1300px',
        numVisible: 4
    },
    {
        breakpoint: '575px',
        numVisible: 1
    }
]);

const selectedImage = ref()
console.log("images", images.value)

const treatmentValue = ref("")
treatmentValue.value = "Cover the soil under the plants with mulch, such as fabric, straw, plastic mulch, or dried leaves. Water at the base of each plant, using drip irrigation, a soaker hose, or careful hand watering. Pruning the bottom leaves can also prevent early blight spores from splashing up from the soil onto leaves."

function onChangeImage(){
    console.log('hi')
}

</script>

<template>
    <div class="row">
        <div class="col-6 ">
            <div class="card images-parent">
                <Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5"
                    containerStyle="max-width: 640px">
                    <template #item="slotProps" >
                        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt"
                            style="width: 100%; display: block" @change="onChangeImage"/>
                    </template>
                    <template #thumbnail="slotProps">
                        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block" />
                    </template>
                    <template #caption="slotProps">
                        <div class="text-xl mb-2 font-bold">{{ slotProps.item.title }}</div>
                        <p class="text-white">{{ slotProps.item.alt }}</p>
                    </template>
                </Galleria>
            </div>
        </div>
        <div class="col-6">
            <div class="row">
                <h1 class="h5"> Treatment (you may edit it to something special)</h1>
            </div>
            <div class="row">
                <div class="card flex justify-content-center text-area-parent">
                    <Textarea v-model="treatmentValue" rows="5" cols="30" />
                </div>
            </div>
            <div class="row">
                <div class="submit-parent">
                    <div class="card flex justify-content-center submit-sub-parent">
                        <Button label="Save the updates" icon="pi pi-check" iconPos="right" class="submit-button" />
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="submit-parent">
                    <div class="card flex justify-content-center submit-sub-parent">
                        <Button label="Declare this location healty" icon="pi pi-check" iconPos="right"
                            class="submit-button" />
                    </div>
                </div>
            </div>
            <div class="row">
                <h1 class="h5"> Treatment period: 20 days</h1>
            </div>
            <div class="row">
                <h1 class="h5"> Started from: 22-10-2020</h1>
            </div>
            <div class="row">
                <h1 class="h5"> End date at: 12-11-2020</h1>
            </div>
            <div class="row align-items-center">
                <div class="col-3">
                    <h1 class="h5"> Extend by: </h1>

                </div>
                <div class="col-3">
                    <div class="flex-auto">
                        <InputNumber v-model="value4" inputId="minmax" :min="0" :max="100" />
                    </div>
                </div>
                <div class="col-6">
                    <div class="extend-parent">
                        <div class="card flex justify-content-center submit-sub-parent">
                            <Button label="Extend" icon="pi pi-check" iconPos="right" class="submit-button" />
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>

</template>

<style scoped>
.text-area-parent {
    margin-right: 70px;
    border-radius: 20px;
}

.images-parent {
    background-color: var(--primary);
    border: none;
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

.row.align-items-center {
    display: flex;
    align-items: center;
    /* Center vertically */
}

.extend-parent{
    display: flex;
    justify-content: center;
}
</style>