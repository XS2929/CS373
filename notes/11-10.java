// -----------
// Fri, 10 Nov
// -----------

/*
Subclassing Movie seems like a good idea, but isn't:
    It would require changing the API.
    It would make it difficult for a new movie to become a regular move.

Better idea is to create Price and subclass it:
    API wouldn't have to change.
    It would be easy to change a new movie to a regular movie.
    Switch statement wouldn't disappear, but it would move to setPriceCode() and run much lest often.
*/
