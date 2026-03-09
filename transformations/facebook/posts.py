import logging
from pathlib import Path
import pandas as pd
import numpy as np
from unidecode import unidecode


_video_titles_to_program = {

    '"The Rain Stopped" (Part II)':'Eucharistic Encounters',
    '"The Rain Stopped."':'Eucharistic Encounters',
    '"The Rain Stopped." (Part II)':'Eucharistic Encounters',
    'Seven words you need to know':'Eucharistic Encounters',
    'The word "August" in the Code of Canon Law':'Eucharistic Encounters',
    'Daily Holy Communion can make you a strong person - Fr. Sal Ferigle':'Eucharistic Encounters',
    'Mass is ended. Now what do we do?':'Lenten Lessons',
    '"The Value of a Mass"':'Eucharistic Encounters',
    '"Secret" prayers at Mass':'Lenten Lessons',
    '"The Rain Stopped."':'Eucharistic Encounters',
    'Malboro Man "And his hands were shaking..."':'Carols of Comfort and Joy',
    'Wassail Song - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Sussex Carol - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Go Tell it on the Mountain - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Lo, How a Rose E\'er Blooming - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Away in a Manger - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    '"That\'s why we had to start in the chapel."':'Eucharistic Encounters',
    'Maria Durch Ein Dornwald Ging - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'O Christmas Tree - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'O little Town of Bethlehem - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Silent Night - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'In Dulci Jubilo - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'The 12 Days of Christmas - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'In the Bleak Midwinter - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Good King Wenceslaus - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'We Three Kings - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'O Holy Night - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'O Come O Come Emmanuel - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'O Come, All Ye Faithful - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Video 12: Generous, courageous, and charitable: Mother Teresa':'Eucharistic Encounters',
    'Jolly Old St. Nicholas - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Hark, the herald angels sing':'Carols of Comfort and Joy',
    'Hark! The Herald Angels Sing - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Angels We Have Heard on High':'Carols of Comfort and Joy',
    'God Rest Ye Merry Gentlemen':'Carols of Comfort and Joy',
    'More Faith Than Money':'Eucharistic Encounters',
    '"That should be your intention."':'Eucharistic Encounters',
    'Caddying for Christ':'Eucharistic Encounters',
    'Generous, courageous, and charitable: St. Damien of Molokai':'Eucharistic Encounters',
    'What\'s the best way to receive Holy Communion?':'Eucharistic Encounters',
    '"Take it to Jesus" Story 5':'Eucharistic Encounters',
    '"And what good hands those are."':'Eucharistic Encounters',
    'The Mysterious Metal Sound - Eucharistic Encounters Video 3':'Eucharistic Encounters',
    'Eucharistic Encounters - Video 3':'Eucharistic Encounters',
    'What it means to show up for Jesus':'Eucharistic Encounters',
    'Do you know how much that will cost?':'Eucharistic Encounters',
    'Walk to Mary Liturgy at the National Shrine of Our Lady of Champion [ LIVE ] May 6, 2023':'Other',
    'Announcement from the Shrine of Our Lady of Good Help':'Other',
    'Great Faith Questions from Great Kids - today on the Patrick Madrid Show!':'Other',
    'After Holy Communion, do this!':'Lenten Lessons',
    'How do you receive Holy Communion?':'Lenten Lessons',
    'We say the words of an unbaptized centurion?':'Lenten Lessons',
    'Remember "secret" prayers?':'Lenten Lessons',
    'This means "Lamb of God"':'Lenten Lessons',
    'How does peace begin?':'Lenten Lessons',
    'There are seven petitions in this prayer':'Lenten Lessons',
    'It\'s the same in multiple languages':'Lenten Lessons',
    'Do you know what the Doxology is?':'Lenten Lessons',
    'Did you know the dead are actually alive?':'Lenten Lessons',
    'Who doesn\'t like bells?':'Lenten Lessons',
    'What did Jesus say at the Last Supper?':'Lenten Lessons',
    'Praying for someone? Remember this!':'Lenten Lessons',
    'Now it is time to kneel because something very important is about to happen.':'Lenten Lessons',
    'It changes daily and by the season....':'Lenten Lessons',
    'This is like saying grace before meals.':'Lenten Lessons',
    '"My sacrifice and yours." What does that mean?':'Lenten Lessons',
    'Can we give something back to God?':'Lenten Lessons',
    'Ask and you shall receive!':'Lenten Lessons',
    'It\'s one of the 7 Great Prayers':'Lenten Lessons',
    'It\'s also known as the sermon.':'Lenten Lessons',
    'This means "Good News"':'Lenten Lessons',
    'Did you know you can speak Hebrew?':'Lenten Lessons',
    'Jesus prayed these too!':'Lenten Lessons',
    '"You may now be seated"':'Lenten Lessons',
    '"Father, read the black, do the red."':'Lenten Lessons',
    'What\'s the number one song ever?':'Lenten Lessons',
    'It\'s Greek for "Lord, have mercy."':'Lenten Lessons',
    'Remember how Beethoven\'s Fifth Symphony begins?':'Lenten Lessons',
    'It\'s like washing your hands before a meal...':'Lenten Lessons',
    'Right before the Ascension, He taught us this...':'Lenten Lessons',
    'You get out of it what you put into it':'Lenten Lessons',
    'Sacred vestments and vessels are kept here...':'Lenten Lessons',
    'Every Catholic Church has this...':'Lenten Lessons',
    '(Hint) It\'s not a table...':'Lenten Lessons',
    'Ever hear of the "Holy of Holies?"':'Lenten Lessons',
    'What\'s a Genuflection?':'Lenten Lessons',
    'Lesson 1: Holy Water':'Lenten Lessons',
    'Wednesday [ First Week of Christmas ] Cathedral of St. Paul':'Mass',
    'Feast of the Immaculate Conception [ LIVE ] December 8, 2022':'Mass',
    'It\'s a Miracle - A Marriage Saved!':'Other',
    'Catholicism ABC\'s (Are you smarter than a 1st grader?)':'Other',
    'The TRIPLE Header!':'Other',
    'Eucharistic Revival':'Other',
    'The Amazing History of Our Lady of Fatima':'Other',
    'Tuesday Trivia 04/26':'Trivia',
    'Divine Mercy Sunday - Live':'Divine Mercy',
    'Good Friday Stations of the Cross [ Relevant Radio ]':'Stations of the Cross',
    'Lesson 37: Behold the Lamb of God':'Lenten Lessons',
    'Lesson 36: The best \'secret\' prayer':'Lenten Lessons',
    'Lesson 35: The Agnus Dei':'Lenten Lessons',
    'Lesson 34: The Sign of Peace':'Lenten Lessons',
    'Lesson 32: Amen!':'Lenten Lessons',
    '31: Eucharistic Doxology':'Lenten Lessons',
    'Memento of the Dead':'Lenten Lessons',
    'Lesson 25: The Preface':'Lenten Lessons',
    'This is like saying grace before meals...':'Lenten Lessons',
    'Lesson 23: The \'Orate Fratres\'':'Lenten Lessons',
    'Consecration of Russia, Ukraine to Immaculate Heart of Mary':'Ukraine Consecration',
    'New event':'Other',

}


def transform(input_filepath: str, output_dir: str) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting transform for: {input_filepath}")
    try:
        df = pd.read_parquet(input_filepath)

        # Fill missing video titles and standardize characters
        logging.info("Filling missing video titles and standardizing characters")
        df['video_title'] = df['video_title'].fillna('No Title').apply(unidecode)

        # Calculate week dates based on datetime columns
        logging.info("Calculating 'published_week_date'.")
        df['published_week_date'] = df['published_datetime'] - pd.to_timedelta(df['published_datetime'].dt.dayofweek, unit='d')

        # Add indicator columns and assign video program
        logging.info("Adding indicator columns based on 'video_title' and assigning video program")
        fraa, mass, chaplet = _get_indicator_columns(df['video_title'])
        df['FRAA_Ind'] = fraa
        df['Mass_Ind'] = mass
        df['Chaplet_Ind'] = chaplet

        logging.info("Assigning 'video_program' and 'video_program_other'.")
        df['video_program'] = _get_video_program(df)
        df['video_program_other'] = df['video_title'].map(_video_titles_to_program)
        df['video_program'] = df['video_program_other'].fillna(df['video_program'])

        # Calculate hour metrics
        logging.info("Calculating hour metrics")
        df['video_duration_hours'] = (df['video_duration_seconds'] / 3600).round(4).fillna(0).astype('float64')
        df['total_hours_viewed'] = (df['total_seconds_viewed'] / 3600).round(4).fillna(0).astype('float64')

        # Fill NAs in all numeric columns with 0
        logging.info("Filling NAs in numeric columns with 0.")
        numeric_columns = df.select_dtypes(include=['number']).columns
        df[numeric_columns] = df[numeric_columns].fillna(0)

        # Convert string columns back to 'string' dtype
        logging.info("Converting string columns back to 'string' dtype.")
        string_columns = df.select_dtypes(include=['object']).columns
        df[string_columns] = df[string_columns].astype('string')

        # Replace NaNs with None
        logging.info("Replacing NaNs with None.")
        df = df.where(pd.notna(df), None)

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        df.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise


def _get_indicator_columns(search_col: pd.Series):
    fraa_ind = search_col.str.contains('rosary', case=False, na=False).astype(int)
    mass_ind = search_col.str.contains('mass', case=False, na=False).astype(int)
    chaplet_ind = search_col.str.contains('chaplet', case=False, na=False).astype(int)
    return fraa_ind, mass_ind, chaplet_ind


def _get_video_program(data: pd.DataFrame, default='Other') -> pd.Series:
    conditions = [
        data['FRAA_Ind'] == 1,
        data['Mass_Ind'] == 1,
        data['Chaplet_Ind'] == 1
    ]
    choices = ['FRAA', 'Mass', 'Chaplet']
    program_array = np.select(conditions, choices, default=default)
    return pd.Series(program_array, index=data.index).astype('string')
