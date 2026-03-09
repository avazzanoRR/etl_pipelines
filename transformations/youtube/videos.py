import logging
from pathlib import Path
from typing import Tuple, Any
import pandas as pd
import numpy as np
from unidecode import unidecode
from dateutil.parser import parse


_video_titles_to_program = {
# Eucharistic Encounters
    '01 - "Do You Know How Much That Will Cost?"':'Eucharistic Encounters',
    '02 - His First Words as Pope were "Do Not be Afraid." That\'s Why he Said, "I\'ll Come."':'Eucharistic Encounters',
    '03 - The Mysterious Metal Sound':'Eucharistic Encounters',
    '03 - The Mysterious Metal Sound #religion #catholicdevotion #eucharisticmiracle  #catholicprayer':'Eucharistic Encounters',
    '"And What Good Hands Those Are."':'Eucharistic Encounters',
    '"And What Good Hands Those Are." #eucharisticmiracle #religion #catholicdevotion':'Eucharistic Encounters',
    'Caddying for Christ':'Eucharistic Encounters',
    'Caddying for Christ #eucharisticmiracle #christmas #catholiccommunity':'Eucharistic Encounters',
    'Eucharistic Encounters 1: Do you know how much that will cost me?':'Eucharistic Encounters',
    'Generous, courageous, and charitable: Mother Teresa':'Eucharistic Encounters',
    'Generous, courageous, and charitable: Mother Teresa #catholicradio':'Eucharistic Encounters',
    'Generous, courageous, and charitable: St. Damien of Molokai':'Eucharistic Encounters',
    'His first words as Pope were "do not be afraid." That\'s why he said, "I\'ll come."':'Eucharistic Encounters',
    'Malboro Man "And his hands were shaking..."':'Eucharistic Encounters',
    'Marlboro Man #eucharisticmiracle #christmas #catholiccommunity':'Eucharistic Encounters',
    'More faith than money':'Eucharistic Encounters',
    'Take it to Jesus':'Eucharistic Encounters',
    'Take it to Jesus #eucharisticmiracle #religion #catholicdevotion #catholicprayer':'Eucharistic Encounters',
    '"That should be your intention"':'Eucharistic Encounters',
    '"That should be your intention."':'Eucharistic Encounters',
    '"That\'s why we had to start in the chapel."':'Eucharistic Encounters',
    '"That\'s why we had to start in the chapel." #eucharisticmiracle #christmas #catholiccommunity':'Eucharistic Encounters',
    'The most beautiful perpetual Adoration Chapel in the world':'Eucharistic Encounters',
    'The most beautiful perpetual Adoration Chapel in the world #eucharisticmiracle #catholicdevotion':'Eucharistic Encounters',
    '"The Rain Stopped."':'Eucharistic Encounters',
    '"The Rain Stopped."':'Eucharistic Encounters',
    'The value of a Mass':'Eucharistic Encounters',
    'What\'s the best way to receive Holy Communion?':'Eucharistic Encounters',
    'What\'s the Best Way to Receive Holy Communion? #eucharisticmiracle #religion':'Eucharistic Encounters',
# Carols of Comfort and Joy
    'Wassail Song - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Sussex Carol - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Go Tell it on the Mountain - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Lo, How a Rose E\'er Blooming - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Away in a Manger - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Maria Durch Ein Dornwald Ging - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'O Christmas Tree - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'O Little Town of Bethlehem - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Silent Night - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'In Dulci Jubilo - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    '12 Days of Christmas - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Joy to the World - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'In the Bleak Midwinter -  Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Good King Wenceslas - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'We Three Kings - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'O Holy Night - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'O Come O Come Emmanuel - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'O Come, All Ye Faithful - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Jolly Old St. Nicholas - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Hark! The Herald Angels Sing - Carols of Comfort and Joy':'Carols of Comfort and Joy',
    'Angels We Have Heard on High':'Carols of Comfort and Joy',
    'God Rest Ye Merry Gentlemen':'Carols of Comfort and Joy',
    'God Rest Ye Merry Gentlemen - Carols of Comfort and Joy':'Carols of Comfort and Joy',
# Lenten Lessons
    'Father Rocky\'s Lenten Lessons on the Mass - Premium Edition':'Lenten Lessons',
    'Lenten Lessons on the Mass - Premium Edition 2022':'Lenten Lessons',
    'Lenten Lessons on the Mass Premium Edition - 01 The Chapel':'Lenten Lessons',
    'Lenten Lessons on the Mass Premium Edition - 02 Baby Jesus':'Lenten Lessons',
    'Lenten Lessons on the Mass Premium Edition - 03 Entering the Chapel':'Lenten Lessons',
    'Lenten Lessons on the Mass Premium Edition - 04 The Sacristy':'Lenten Lessons',
    'Lenten Lessons on the Mass Premium Edition - 05 Sacred Vestments':'Lenten Lessons',
    'Lenten Lesson 26 The Eucharistic Prayer':'Lenten Lessons',
    '2022 Lenten Lesson 40: Mass is ended. Now what do we do?':'Lenten Lessons',
    '2022 Lenten Lesson 37: We say the words of an unbaptized centurion?':'Lenten Lessons',
    '2022 Lenten Lesson 35: This means "Lamb of God"':'Lenten Lessons',
    '2022 Lenten Lessons 34: How does peace begin?':'Lenten Lessons',
    '2022 Lenten Lesson 33: The Lord\'s Prayer':'Lenten Lessons',
    '2022 Lenten Lesson 32: Can I get an "Amen" for that?':'Lenten Lessons',
    '2022 Lenten Lesson 30: Did you know the dead are actually alive?':'Lenten Lessons',
    '2022 Lenten Lesson 31: Do you know what the Doxology is?':'Lenten Lessons',
    '2022 Lenten Lessons 29 Who doesn\'t like bells?':'Lenten Lessons',
    '2022 Lenten Lessons 28: What did Jesus say at the Last Supper?':'Lenten Lessons',
    '2022 Lenten Lessons 27 Praying for someone? Remember this!':'Lenten Lessons',
    '2022 Lenten Lesson 25: The Preface':'Lenten Lessons',
    '2022 Lenten Lessons 24: Prayer Over the Gifts':'Lenten Lessons',
    '2022 Lenten Lesson 23: The \'Orate Fratres\'':'Lenten Lessons',
    '2022 Lenten Lesson 22: The \'Secret\' Prayers':'Lenten Lessons',
    '2022 Lenten Lesson 21: The Offertory':'Lenten Lessons',
    '2022 Lenten Lesson 20: Prayers of the Faithful':'Lenten Lessons',
    '2022 Lenten Lessons 19 The Profession of Faith':'Lenten Lessons',
    '2022 Lenten Lessons 18: The Homily':'Lenten Lessons',
    '2022 Lenten Lesson 16: Alleluia':'Lenten Lessons',
    'Lesson 36: Remember \'secret\' prayers? This is the best one!':'Lenten Lessons',
    'Lesson 17: The Gospel':'Lenten Lessons',
    'Lesson 14: The First Reading':'Lenten Lessons',
    'Lesson 15: Jesus prayed these too!':'Lenten Lessons',
    'Lesson 13: The Collect':'Lenten Lessons',
    'Lesson 11: It\'s Greek for "Lord, have mercy."':'Lenten Lessons',
    'Lesson 10: Remember how Beethoven\'s Fifth Symphony begins?':'Lenten Lessons',
    'Lesson 9: It\'s like washing your hands before a meal':'Lenten Lessons',
    'Lesson 8: Right before the Ascension, He taught us this...':'Lenten Lessons',
    'Lesson 7: Prayers Before Mass':'Lenten Lessons',
    'Lesson 6: Sacred vestments and vessels are kept here...':'Lenten Lessons',
    'Lesson 5: Every Catholic Church has this...':'Lenten Lessons',
    'Lesson 4: (Hint) It\'s not a table...':'Lenten Lessons',
    'Lesson 3: Ever hear of the "Holy of Holies?" - The Tabernacle':'Lenten Lessons',
    'Lesson 2: At the name of Jesus, do this - Genuflection':'Lenten Lessons',
    'Lesson 1: Protect Yourself - Use Holy Water':'Lenten Lessons',
    'Lesson 1: Holy Water':'Lenten Lessons',
    '(Hint) It\'s not a table...':'Lenten Lessons',
    'After Holy Communion, do this!':'Lenten Lessons',
    'Ask and you shall receive!':'Lenten Lessons',
    'Can we give something back to God?':'Lenten Lessons',
    'Do you know what the Doxology is?':'Lenten Lessons',
    'Did you know the dead are actually alive?':'Lenten Lessons',
    'Did you know you can speak Hebrew?':'Lenten Lessons',
    'Every Catholic Church has this...':'Lenten Lessons',
    'Ever hear of the "Holy of Holies?"':'Lenten Lessons',
    '"Father, read the black, do the red."':'Lenten Lessons',
    'How do you receive Holy Communion?':'Lenten Lessons',
    'How does peace begin?':'Lenten Lessons',
    'It changes daily and by the season....':'Lenten Lessons',
    'It\'s one of the 7 Great Prayers':'Lenten Lessons',
    'It\'s also known as the sermon.':'Lenten Lessons',
    'It\'s the same in multiple languages':'Lenten Lessons',
    'It\'s Greek for "Lord, have mercy."':'Lenten Lessons',
    'It\'s like washing your hands before a meal...':'Lenten Lessons',
    'Jesus prayed these too!':'Lenten Lessons',
    'Mass is ended. Now what do we do?':'Lenten Lessons',
    '"My sacrifice and yours." What does that mean?':'Lenten Lessons',
    'Now it is time to kneel because something very important is about to happen.':'Lenten Lessons',
    'Praying for someone? Remember this!':'Lenten Lessons',
    'Remember "secret" prayers?':'Lenten Lessons',
    'Remember how Beethoven\'s Fifth Symphony begins?':'Lenten Lessons',
    'Right before the Ascension, He taught us this...':'Lenten Lessons',
    'Sacred vestments and vessels are kept here...':'Lenten Lessons',
    '"Secret" prayers at Mass':'Lenten Lessons',
    'This is like saying grace before meals.':'Lenten Lessons',
    'This means "Good News"':'Lenten Lessons',
    'This means "Lamb of God"':'Lenten Lessons',
    'There are seven petitions in this prayer':'Lenten Lessons',
    'We say the words of an unbaptized centurion?':'Lenten Lessons',
    'Who doesn\'t like bells?':'Lenten Lessons',
    'What\'s the number one song ever?':'Lenten Lessons',
    'What\'s a Genuflection?':'Lenten Lessons',
    'What did Jesus say at the Last Supper?':'Lenten Lessons',
    '"You may now be seated"':'Lenten Lessons',
    'You get out of it what you put into it':'Lenten Lessons',
# Other
    'Bishop David Ricken\'s Assumption Mass Sermon':'Other',
}


def transform(input_filepath: str, output_dir: str) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting transform for: {input_filepath}")
    try:
        df = pd.read_parquet(input_filepath)

        # Convert 'video_published_date' to datetime
        logging.info("Converting 'video_published_date' to datetime.")
        df['video_published_date'] = df['video_published_date'].apply(_parse_mixed_formats)

        # Drop rows where 'video_published_date' is NaT (not a time)
        logging.info("Dropping rows where 'video_published_date' is NaT.")
        df = df.dropna(subset=['video_published_date']).copy()

        # Calculate the reporting week start date
        logging.info("Calculating the reporting week start date basd on 'video_published_date'.")
        df['video_published_week_date'] = _get_reporting_week(df['video_published_date'])

        # Add indicator columns and assign video program
        logging.info("Adding indicator columns based on 'video_title'.")
        fraa, mass, chaplet = _get_indicator_columns(df['video_title'])
        df['FRAA_Ind'] = fraa
        df['Mass_Ind'] = mass
        df['Chaplet_Ind'] = chaplet

        df['video_program'] = _get_video_program(df)
        df['video_program_other'] = df['video_title'].map(_video_titles_to_program)
        df['video_program'] = df['video_program_other'].fillna(df['video_program'])

        # Clean the video title column
        logging.info("Cleaning the 'video_title' column.")
        df['video_title'] = df['video_title'].str.strip().apply(unidecode).str.strip()

        # Recast string columns that went through transformations (to ensure they are 'string' dtype instead of 'object')
        logging.info("Recasting string columns to 'string' dtype")
        string_columns = ['video_title', 'video_program', 'video_program_other']
        df[string_columns] = df[string_columns].astype('string')

        # Fill NAs in all numeric columns with 0
        logging.info("Filling NAs in numeric columns with 0.")
        numeric_columns = df.select_dtypes(include=['number']).columns
        df[numeric_columns] = df[numeric_columns].fillna(0)

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


def _parse_mixed_formats(date_str):
    for fmt in ('%d-%b-%y', '%Y-%m-%d', '%d/%m/%Y'):
        try:
            return pd.to_datetime(date_str, format=fmt)
        except ValueError:
            continue
    # Fallback to more flexible parsing
    try:
        return parse(date_str, dayfirst=True)
    except ValueError:
        return pd.NaT


def _get_reporting_week(date_col: pd.Series) -> pd.Series:
    date_col = pd.to_datetime(date_col)
    return date_col - pd.to_timedelta(date_col.dt.dayofweek, unit='d')


def _get_indicator_columns(search_col: pd.Series) -> Tuple[pd.Series, pd.Series, pd.Series]:
    fraa_ind = search_col.str.contains('rosary', case=False, na=False).astype(int)
    mass_ind = search_col.str.contains('mass', case=False, na=False).astype(int)
    chaplet_ind = search_col.str.contains('chaplet', case=False, na=False).astype(int)
    return fraa_ind, mass_ind, chaplet_ind


def _get_video_program(data: pd.DataFrame, default: Any = 'Other') -> pd.Series:
    conditions = [
        data['FRAA_Ind'] == 1,
        data['Mass_Ind'] == 1,
        data['Chaplet_Ind'] == 1
    ]
    choices = ['FRAA', 'Mass', 'Chaplet']
    program_array = np.select(conditions, choices, default=default)
    return pd.Series(program_array, index=data.index).astype('string')
