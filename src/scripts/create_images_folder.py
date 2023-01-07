import os

def create_image_folder():
    """This method creates the images folder and all the subfolders."""
    if not os.path.exists('images'):
        os.makedirs('images')
        for section in ['second_section', 'third_section', 'fourth_section', 'fifth_section']:
            for device in ['chromecast', 'smart_tv']:
                subfolder = f'images{os.sep}{section}{os.sep}{device}'
                if section == 'second_section':
                    os.makedirs(f'{subfolder}{os.sep}boxplot')
                    os.makedirs(f'{subfolder}{os.sep}histogram')
                    os.makedirs(f'{subfolder}{os.sep}edf')
                elif section == 'third_section':
                    os.makedirs(f'{subfolder}{os.sep}boxplot')
                    os.makedirs(f'{subfolder}{os.sep}statistical_analysis')
                elif section == 'fourth_section':
                    os.makedirs(f'{subfolder}{os.sep}histogram')
                    os.makedirs(f'{subfolder}{os.sep}histogram_mle')
                    os.makedirs(f'{subfolder}{os.sep}probability_plot')
                elif section == 'fifth_section':
                    os.makedirs(f'{subfolder}{os.sep}scatter_plot')

if __name__ == '__main__':
    create_image_folder()