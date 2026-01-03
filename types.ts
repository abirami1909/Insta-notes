
export interface ImportantTerm {
  term: string;
  definition: string;
}

export interface Summary {
  keyPoints: string[];
  quickRevision: string[];
  importantTerms: ImportantTerm[];
}

export interface Note {
  id: string;
  title: string;
  videoUrl: string;
  thumbnail: string;
  date: string;
  subject: string;
  summary: Summary;
}

export enum AppRoute {
  Splash = '/',
  Login = '/login',
  Home = '/home',
  Summary = '/summary',
  Saved = '/saved'
}
