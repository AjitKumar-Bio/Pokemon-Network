% Load the similarity data from file
similarity_data = readmatrix('gs_similarity.txt', 'Delimiter', ',');

% Create a new empty graph
G = graph();

% Add nodes for each Pokemon
for i = 1:size(similarity_data, 1)

    pokemon1 = string(similarity_data(i, 1));
    pokemon2 = string(similarity_data(i, 2));
    G = addnode(G, pokemon1);
    G = addnode(G, pokemon2);
end

% Add edges between similar Pokemon
for i = 1:size(similarity_data, 1)
    pokemon1 = string(similarity_data(i, 1));
    pokemon2 = string(similarity_data(i, 2));
    similarity = similarity_data(i, 3);
    if similarity > 0.9
        G = addedge(G, pokemon1, pokemon2);
    end
end

% Plot the graph
plot(G);

