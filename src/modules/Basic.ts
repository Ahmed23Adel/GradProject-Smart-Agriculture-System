import Cookies from 'js-cookie';

export class UserType {
    private static instance: UserType;
    private is_owner: boolean;

    private constructor() {
        if (this.getCookie("type") === "owner") {
            this.is_owner = true;
        } else {
            this.is_owner = false;
        }
    }

    public static getInstance(): UserType {
        if (!UserType.instance) {
            UserType.instance = new UserType();
        }
        return UserType.instance;
    }

    private getCookie(key: string): string | undefined {
        return Cookies.get(key);
    }

    public getUserType(): boolean {
        return this.is_owner;
    }
    public getUserId(): string | undefined {
        return this.getCookie("user_id")
    }
}

export function findCoordinates(maxLong, minLong, maxLat, minLat, zoneSize, zoneNameSearch, calculatedCoordinates){
    const horizontalZones = Math.ceil((maxLong - minLong) * 111139 / zoneSize);
    const verticalZones = Math.ceil((maxLat - minLat) * 111139 / zoneSize);
    const maxZoneIndex = horizontalZones * verticalZones - 1; // Maximum valid zone index

    if (zoneNameSearch) {
        let inputValue = zoneNameSearch.trim();

        let zoneNumber;
        // Check if input starts with "Zone " followed by an integer
        const zonePattern = /^zone\s+(\d+)$/i; // Case insensitive
        const match = inputValue.match(zonePattern);

        if (match) {
            // Extract the integer part after "Zone "
            zoneNumber = Number(match[1]);
        } else if (/^\d+$/.test(inputValue)) {
            // If input is a single integer
            zoneNumber = Number(inputValue);
        } else {
            // If input does not follow the required format, set calculatedCoordinates to empty strings
            calculatedCoordinates.value = { long: "", lat: "" };
            return;
        }

        // Validate zoneNumber
        if (zoneNumber <= 0 || zoneNumber > maxZoneIndex) {
            // If zoneNumber is not valid, set calculatedCoordinates to empty strings
            calculatedCoordinates.value = { long: "", lat: "" };
            return;
        }

        // Calculate row and column indices from zoneNumber
        const rowIndex = Math.floor(zoneNumber / horizontalZones);
        const colIndex = zoneNumber % horizontalZones;

        console.log("rowIndex, colIndex", rowIndex, colIndex);

        const long = minLong + colIndex * zoneSize / 111139;
        const lat = minLat + rowIndex * zoneSize / 111139;
        calculatedCoordinates.value = { long, lat };
    } else {
        // If zoneNameSearch.value is empty, set calculatedCoordinates to empty strings
        calculatedCoordinates.value = { long: "", lat: "" };
    }
}

export function openGoogleMapsWithLatLong(calculatedCoordinates) {
    const googleMapsLink = `https://www.google.com/maps?q=${calculatedCoordinates.lat},${calculatedCoordinates.long}`;
    window.open(googleMapsLink, '_blank');
}

export function deleteCookie (key: string){
    Cookies.remove(key);
}


export function formatDate(date: Date) {
    const month = date.getMonth() + 1; // Months are 0-based, so add 1
    const day = date.getDate();
    const year = date.getFullYear();
    // Pad month and  with leading zeros if necessary
    const paddedMonth = month.toString().padStart(2, '0');
    const paddedDay = day.toString().padStart(2, '0');
    // Return the formatted date as a string
    return `${paddedDay}-${paddedMonth}-${year}`;
}