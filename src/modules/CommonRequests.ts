import { HttpRequester } from '@/services/ApiCaller.ts';
import type { Ref, reactive } from 'vue'; // Import necessary types
 // Import necessary types

export async function fetchAllLocations(locations: Ref<any[]>, selectedLocation: Ref<any>, isLocationNewForExpert: Ref<any[]>, zonesTreatment: Ref<any[]>) {
    const requester = new HttpRequester('diseased-zones');
    locations.value = [];
    await requester.callApi("GET").then(requester_data => {
        console.log("requester_data", requester_data)
        for (const loc of requester_data.locations) {
            locations.value.push({ name: loc.Zone_Name });
            isLocationNewForExpert.value.push(!loc.Checked_By_Expert);
            zonesTreatment.value.push(loc.Treatment)
        }
        // selectedLocation.value = locations.value[0];
        return locations.value[0].name;
    }).catch(error => {
        console.error("Error fetching locations:", error);
    });

}
