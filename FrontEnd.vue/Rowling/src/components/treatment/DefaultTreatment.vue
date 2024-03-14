<script setup>
import {defineProps} from "vue"
import { ref } from 'vue';

const {diseaesName} = defineProps(['diseaesName','backColor'])
console.log(diseaesName)
// const diseaesName = ref("Early blight");

// document.addEventListener('DOMContentLoaded', function () {
//     var maxLength = 20;
//     var default_text = document.getElementById('blight-text');
//     var readMoreLink = document.getElementById('read-more-link');

//     var content = default_text.textContent;
//     if (content.length > maxLength) {
//         default_text.textContent = content.slice(0, maxLength) + "...";
//         readMoreLink.style.display = 'inline';
//         readMoreLink.addEventListener('click', function (event) {
//             event.preventDefault();
//             if (default_text.textContent.length === maxLength) {
//                 default_text.textContent = content;
//                 readMoreLink.textContent = 'Read Less';
//             } else {
//                 default_text.textContent = content.slice(0, maxLength);
//                 readMoreLink.textContent = 'Read More';
//             }
//         });
//     }
// });

</script>

<template>
    <!-- Cover the soil under the plants with mulch, such as fabric, straw,
    plastic mulch, or dried leaves. Water at the base of each plant, using drip irrigation, a soaker hose,
    or careful hand watering. Pruning the bottom leaves can also prevent early blight spores from splashing
    up from the soil onto leaves. -->
    <div class="card card-border" style="width: 12rem; background-color:#F4EDCC; border-radius: 20%;">
        <img src='/src/assets/images/treatment/treatment.png' class="card-img-top card-img" alt="...">
        <div class="card-body">
            <!-- <h5 class="card-title">{{ diseaesName }} default treatment</h5> -->
            <h5 class="card-title">{{diseaesName}} default treatment</h5>
            <p class="card-text" id="blight-text" max-length="20">Cover the soil under...</p>
            <a href="#" id="read-more-link" class="btn btn-primary read-more">Read More</a>
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

.read-more {
    margin-left: 10px;
}

.card-border:hover {
    transform: scale(110%);
    cursor: pointer;
}
</style>