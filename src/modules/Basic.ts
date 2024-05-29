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