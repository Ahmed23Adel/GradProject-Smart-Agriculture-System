<script setup>
import {defineProps} from "vue"
import { ref } from 'vue';

const {diseaesName, backColor, diseaseId} = defineProps(['diseaesName','backColor', 'diseaseId'])

const toRef = ref("")
toRef.value = "/treatment/disease-default-treatment/" + diseaseId;

</script>

<template>
    <div class="card wobble-horizontal" style="width: 12rem; background-color:#F4EDCC; border-radius: 20%;">
        <img src='/src/assets/images/treatment/treatment.png' class="card-img-top card-img" alt="...">
        <div class="card-body">
            <!-- <h5 class="card-title">{{ diseaesName }} default treatment</h5> -->
            <h5 class="card-title">{{diseaesName}} default treatment</h5>
            <p class="card-text" id="blight-text" max-length="20">Cover the soil under...</p>
			<router-link :to="toRef"><a href="#" id="read-more-link" class="btn btn-primary read-more">Read More</a></router-link>
            
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
@keyframes wobble-horizontal {
	16.65% {
		transform: translateX(8px);
	}

	33.3% {
		transform: translateX(-6px);
	}

	49.95% {
		transform: translateX(4px);
	}

	66.6% {
		transform: translateX(-2px);
	}

	83.25% {
		transform: translateX(1px);
	}

	100% {
		transform: translateX(0);
	}
}
.wobble-horizontal {
	display: inline-block;

	@include hideTapHighlightColor();
	@include hardwareAccel();
	@include improveAntiAlias();

	&:hover {
		animation-name: wobble-horizontal;
		animation-duration: 1s;
		animation-timing-function: ease-in-out;
		animation-iteration-count: 1;
	}
}
</style>