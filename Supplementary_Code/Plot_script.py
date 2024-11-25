from pycirclize import Circos
import pandas as pd
import glob

def read_karyotype(file_path):
    """Reads karyotype file to get chromosome IDs, lengths, and colors."""
    karyotype = pd.read_csv(file_path, sep=' ', header=None, names=['chrom_id', 'label', 'length', 'color'])
    
    karyotype['short_chrom_id'] = karyotype['chrom_id'].apply(lambda x: x.split('_')[-1])
    
    return karyotype[['chrom_id', 'short_chrom_id', 'length', 'color']]

def read_links(file_path):
    """Reads links file to get recombination link data between chromosomes."""
    links = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            chrom1, start1, end1 = parts[0], int(parts[1]), int(parts[2])
            chrom2, start2, end2 = parts[3], int(parts[4]), int(parts[5])
            color = parts[6].split('=')[1]  
            links.append((chrom1, start1, end1, chrom2, start2, end2, color))
    return links

def read_proximity_files(proximity_folder):
    """Reads all proximity files and assigns positions to chromosomes in both genomes."""
    proximity_data = []
    file_paths = glob.glob(f"{proximity_folder}/*.txt") 
    for file_path in file_paths:
        chrom = file_path.split('/')[-1].replace('proximity_', '').replace('.txt', '')  
        
        # Read positions from file and assign to both genomes
        positions = pd.read_csv(file_path, header=None, names=['position'])
        positions['genome1'] = f"genome1_{chrom}"
        positions['genome2'] = f"genome2_{chrom}"
        proximity_data.append(positions)
        
    return pd.concat(proximity_data, ignore_index=True)

def create_circos_plot(karyotype_file, links_file, proximity_folder):
   
    karyotype = read_karyotype(karyotype_file)
    links = read_links(links_file)
    proximity = read_proximity_files(proximity_folder)
    
    sectors = {row['chrom_id']: row['length'] for _, row in karyotype.iterrows()}
    
    circos = Circos(sectors=sectors, space=3)
    circos.text("Overlap of recombination hotspots with regions of spatial proximity", deg=360, r=125, size=12)
    
    chr_name2color = {row['chrom_id']: row['color'] for _, row in karyotype.iterrows()}

    for sector in circos.sectors:
        chrom_id = sector.name
        chrom_color = chr_name2color[chrom_id]
        short_chrom_id = karyotype.loc[karyotype['chrom_id'] == chrom_id, 'short_chrom_id'].values[0]
        
        sector.axis(fc="none", ls="solid", lw=2, alpha=0.5)
        sector.text(f"{short_chrom_id}", size=10, color=chrom_color)

        if "genome1" in chrom_id:
            track1 = sector.add_track((75, 100)) 
            track1.axis(fc="tomato", alpha=0.8)  
            
        elif "genome2" in chrom_id:
            track2 = sector.add_track((45, 70)) 
            track2.axis(fc="cyan", alpha=0.8)  
           

    for _, row in proximity.iterrows():
        position = row['position']
        genome1, genome2 = row['genome1'], row['genome2']
        
        if genome1 in sectors:
            sector = circos.get_sector(genome1)
            if sector._tracks.__contains__("genome1_track"):  
                track = sector.get_track("genome1_track")
                
        
        if genome2 in sectors:
            sector = circos.get_sector(genome2)
            if sector._tracks.__contains__("genome2_track"): 
                track = sector.get_track("genome2_track")
               
    for chrom1, start1, end1, chrom2, start2, end2, color in links:
        region1 = (chrom1, start1, end1)
        region2 = (chrom2, start2, end2)
        circos.link(region1, region2, color=color, alpha=0.7, lw=0.6)

   
    circos.savefig("name_of_outputfile")

create_circos_plot('path_to_karyotype.txt_file', 'path_to_links.txt_file','/path_to_chrom_proximity_files' )





