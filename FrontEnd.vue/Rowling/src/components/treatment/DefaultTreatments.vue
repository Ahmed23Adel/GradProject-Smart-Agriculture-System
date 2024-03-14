<script setup>
import DefaultTreatment from "./DefaultTreatment.vue";

</script>
<template>
    <div class="row">
        <div class="col-2">
            <DefaultTreatment :diseaesName="'Early blight'" :backColor="'#F4EDCC'"/>
        </div>
        <div class="col-2">
            <DefaultTreatment :diseaesName="'Late blight'" :backColor="'#A4CE95'"/>
        </div>
        <div class="col-3">
        </div>
        <div class="col-3">
        </div>
    </div>
</template>