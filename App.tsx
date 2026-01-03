
import React, { useState, useEffect } from 'react';
import { Routes, Route, useNavigate, useLocation } from 'react-router-dom';
import SplashScreen from './views/SplashScreen';
import LoginScreen from './views/LoginScreen';
import HomeScreen from './views/HomeScreen';
import SummaryScreen from './views/SummaryScreen';
import SavedNotesScreen from './views/SavedNotesScreen';
import { Note, AppRoute } from './types';

const App: React.FC = () => {
  const [savedNotes, setSavedNotes] = useState<Note[]>([]);
  const [currentNote, setCurrentNote] = useState<Note | null>(null);
  const location = useLocation();

  const handleSaveNote = (note: Note) => {
    setSavedNotes(prev => [note, ...prev]);
  };

  return (
    <div className="mobile-container overflow-hidden flex flex-col">
      <Routes>
        <Route path={AppRoute.Splash} element={<SplashScreen />} />
        <Route path={AppRoute.Login} element={<LoginScreen />} />
        <Route path={AppRoute.Home} element={<HomeScreen onNoteGenerated={(note) => setCurrentNote(note)} />} />
        <Route 
          path={AppRoute.Summary} 
          element={<SummaryScreen note={currentNote} onSave={handleSaveNote} />} 
        />
        <Route 
          path={AppRoute.Saved} 
          element={<SavedNotesScreen notes={savedNotes} onSelectNote={(note) => setCurrentNote(note)} />} 
        />
      </Routes>
    </div>
  );
};

export default App;
