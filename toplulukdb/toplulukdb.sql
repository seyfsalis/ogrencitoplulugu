PGDMP         6            
    x         
   toplulukdb    13.0    13.0 ?    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                        0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    17132 
   toplulukdb    DATABASE     g   CREATE DATABASE toplulukdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Turkish_Turkey.1254';
    DROP DATABASE toplulukdb;
                postgres    false            �            1259    17156 	   duyurular    TABLE     �   CREATE TABLE public.duyurular (
    id integer NOT NULL,
    baslik character varying(99) NOT NULL,
    icerik text NOT NULL,
    tarih date NOT NULL,
    kullanici_id integer NOT NULL,
    grup_id integer NOT NULL
);
    DROP TABLE public.duyurular;
       public         heap    postgres    false            �            1259    17154    duyurular_id_seq    SEQUENCE     �   CREATE SEQUENCE public.duyurular_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.duyurular_id_seq;
       public          postgres    false    203                       0    0    duyurular_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.duyurular_id_seq OWNED BY public.duyurular.id;
          public          postgres    false    202            �            1259    17177    etkinlikler    TABLE     �   CREATE TABLE public.etkinlikler (
    id integer NOT NULL,
    baslik character varying(99) NOT NULL,
    icerik text NOT NULL,
    mekan character varying(99) NOT NULL,
    kullanici_id integer NOT NULL,
    grup_id integer NOT NULL
);
    DROP TABLE public.etkinlikler;
       public         heap    postgres    false            �            1259    17175    etkinlikler_id_seq    SEQUENCE     �   CREATE SEQUENCE public.etkinlikler_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.etkinlikler_id_seq;
       public          postgres    false    205                       0    0    etkinlikler_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.etkinlikler_id_seq OWNED BY public.etkinlikler.id;
          public          postgres    false    204            �            1259    17189    forumlar    TABLE     �   CREATE TABLE public.forumlar (
    id integer NOT NULL,
    baslik character varying(99) NOT NULL,
    icerik text NOT NULL,
    kullanici_id integer NOT NULL,
    grup_id integer NOT NULL
);
    DROP TABLE public.forumlar;
       public         heap    postgres    false            �            1259    17187    forumlar_id_seq    SEQUENCE     �   CREATE SEQUENCE public.forumlar_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.forumlar_id_seq;
       public          postgres    false    207                       0    0    forumlar_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.forumlar_id_seq OWNED BY public.forumlar.id;
          public          postgres    false    206            �            1259    17201 	   galeriler    TABLE     �   CREATE TABLE public.galeriler (
    id integer NOT NULL,
    yol character varying(99) NOT NULL,
    kullanici_id integer NOT NULL,
    grup_id integer NOT NULL
);
    DROP TABLE public.galeriler;
       public         heap    postgres    false            �            1259    17199    galeriler_id_seq    SEQUENCE     �   CREATE SEQUENCE public.galeriler_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.galeriler_id_seq;
       public          postgres    false    209                       0    0    galeriler_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.galeriler_id_seq OWNED BY public.galeriler.id;
          public          postgres    false    208            �            1259    17254    gruplar    TABLE     `   CREATE TABLE public.gruplar (
    id integer NOT NULL,
    ad character varying(55) NOT NULL
);
    DROP TABLE public.gruplar;
       public         heap    postgres    false            �            1259    17252    gruplar_id_seq    SEQUENCE     �   CREATE SEQUENCE public.gruplar_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.gruplar_id_seq;
       public          postgres    false    213                       0    0    gruplar_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.gruplar_id_seq OWNED BY public.gruplar.id;
          public          postgres    false    212            �            1259    17285    kayitlar    TABLE     {   CREATE TABLE public.kayitlar (
    id integer NOT NULL,
    kullanici_id integer NOT NULL,
    grup_id integer NOT NULL
);
    DROP TABLE public.kayitlar;
       public         heap    postgres    false            �            1259    17283    kayitlar_id_seq    SEQUENCE     �   CREATE SEQUENCE public.kayitlar_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.kayitlar_id_seq;
       public          postgres    false    215                       0    0    kayitlar_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.kayitlar_id_seq OWNED BY public.kayitlar.id;
          public          postgres    false    214            �            1259    17229    kullanicilar    TABLE     k  CREATE TABLE public.kullanicilar (
    id integer NOT NULL,
    ad character varying(20) NOT NULL,
    soyad character varying(20) NOT NULL,
    telefon character varying(11) NOT NULL,
    okul_no character varying(15),
    tc character varying(11) NOT NULL,
    mail character varying(55) NOT NULL,
    sifre character varying(55) NOT NULL,
    yetki integer
);
     DROP TABLE public.kullanicilar;
       public         heap    postgres    false            �            1259    17227    kullanicilar_id_seq    SEQUENCE     �   CREATE SEQUENCE public.kullanicilar_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.kullanicilar_id_seq;
       public          postgres    false    211                       0    0    kullanicilar_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.kullanicilar_id_seq OWNED BY public.kullanicilar.id;
          public          postgres    false    210            �            1259    17147    yetki    TABLE     j   CREATE TABLE public.yetki (
    id integer NOT NULL,
    yetki_derecesi character varying(20) NOT NULL
);
    DROP TABLE public.yetki;
       public         heap    postgres    false            �            1259    17145    yetki_id_seq    SEQUENCE     �   CREATE SEQUENCE public.yetki_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.yetki_id_seq;
       public          postgres    false    201            	           0    0    yetki_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.yetki_id_seq OWNED BY public.yetki.id;
          public          postgres    false    200            P           2604    17159    duyurular id    DEFAULT     l   ALTER TABLE ONLY public.duyurular ALTER COLUMN id SET DEFAULT nextval('public.duyurular_id_seq'::regclass);
 ;   ALTER TABLE public.duyurular ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    202    203    203            Q           2604    17180    etkinlikler id    DEFAULT     p   ALTER TABLE ONLY public.etkinlikler ALTER COLUMN id SET DEFAULT nextval('public.etkinlikler_id_seq'::regclass);
 =   ALTER TABLE public.etkinlikler ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    205    204    205            R           2604    17192    forumlar id    DEFAULT     j   ALTER TABLE ONLY public.forumlar ALTER COLUMN id SET DEFAULT nextval('public.forumlar_id_seq'::regclass);
 :   ALTER TABLE public.forumlar ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    206    207    207            S           2604    17204    galeriler id    DEFAULT     l   ALTER TABLE ONLY public.galeriler ALTER COLUMN id SET DEFAULT nextval('public.galeriler_id_seq'::regclass);
 ;   ALTER TABLE public.galeriler ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    208    209            T           2604    17257 
   gruplar id    DEFAULT     h   ALTER TABLE ONLY public.gruplar ALTER COLUMN id SET DEFAULT nextval('public.gruplar_id_seq'::regclass);
 9   ALTER TABLE public.gruplar ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    212    213    213            U           2604    17288    kayitlar id    DEFAULT     j   ALTER TABLE ONLY public.kayitlar ALTER COLUMN id SET DEFAULT nextval('public.kayitlar_id_seq'::regclass);
 :   ALTER TABLE public.kayitlar ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214    215            O           2604    17150    yetki id    DEFAULT     d   ALTER TABLE ONLY public.yetki ALTER COLUMN id SET DEFAULT nextval('public.yetki_id_seq'::regclass);
 7   ALTER TABLE public.yetki ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    200    201    201            [           2606    17165    duyurular duyurular_pk 
   CONSTRAINT     T   ALTER TABLE ONLY public.duyurular
    ADD CONSTRAINT duyurular_pk PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.duyurular DROP CONSTRAINT duyurular_pk;
       public            postgres    false    203            `           2606    17186    etkinlikler etkinlikler_pk 
   CONSTRAINT     X   ALTER TABLE ONLY public.etkinlikler
    ADD CONSTRAINT etkinlikler_pk PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.etkinlikler DROP CONSTRAINT etkinlikler_pk;
       public            postgres    false    205            c           2606    17198    forumlar forumlar_pk 
   CONSTRAINT     R   ALTER TABLE ONLY public.forumlar
    ADD CONSTRAINT forumlar_pk PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.forumlar DROP CONSTRAINT forumlar_pk;
       public            postgres    false    207            f           2606    17207    galeriler galeriler_pk 
   CONSTRAINT     T   ALTER TABLE ONLY public.galeriler
    ADD CONSTRAINT galeriler_pk PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.galeriler DROP CONSTRAINT galeriler_pk;
       public            postgres    false    209            k           2606    17259    gruplar gruplar_pk 
   CONSTRAINT     P   ALTER TABLE ONLY public.gruplar
    ADD CONSTRAINT gruplar_pk PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.gruplar DROP CONSTRAINT gruplar_pk;
       public            postgres    false    213            n           2606    17291    kayitlar kayitlar_pk 
   CONSTRAINT     R   ALTER TABLE ONLY public.kayitlar
    ADD CONSTRAINT kayitlar_pk PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.kayitlar DROP CONSTRAINT kayitlar_pk;
       public            postgres    false    215            i           2606    17234    kullanicilar kullanicilar_pk 
   CONSTRAINT     Z   ALTER TABLE ONLY public.kullanicilar
    ADD CONSTRAINT kullanicilar_pk PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.kullanicilar DROP CONSTRAINT kullanicilar_pk;
       public            postgres    false    211            X           2606    17153    yetki yetki_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.yetki
    ADD CONSTRAINT yetki_pk PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.yetki DROP CONSTRAINT yetki_pk;
       public            postgres    false    201            Y           1259    17163    duyurular_id_uindex    INDEX     N   CREATE UNIQUE INDEX duyurular_id_uindex ON public.duyurular USING btree (id);
 '   DROP INDEX public.duyurular_id_uindex;
       public            postgres    false    203            ^           1259    17184    etkinlikler_id_uindex    INDEX     R   CREATE UNIQUE INDEX etkinlikler_id_uindex ON public.etkinlikler USING btree (id);
 )   DROP INDEX public.etkinlikler_id_uindex;
       public            postgres    false    205            \           1259    17277    fki_duyuru_grup_foreign    INDEX     P   CREATE INDEX fki_duyuru_grup_foreign ON public.duyurular USING btree (grup_id);
 +   DROP INDEX public.fki_duyuru_grup_foreign;
       public            postgres    false    203            ]           1259    17271    fki_duyuru_kullanici_foreign    INDEX     Z   CREATE INDEX fki_duyuru_kullanici_foreign ON public.duyurular USING btree (kullanici_id);
 0   DROP INDEX public.fki_duyuru_kullanici_foreign;
       public            postgres    false    203            g           1259    17265 	   fki_yetki    INDEX     C   CREATE INDEX fki_yetki ON public.kullanicilar USING btree (yetki);
    DROP INDEX public.fki_yetki;
       public            postgres    false    211            a           1259    17196    forumlar_id_uindex    INDEX     L   CREATE UNIQUE INDEX forumlar_id_uindex ON public.forumlar USING btree (id);
 &   DROP INDEX public.forumlar_id_uindex;
       public            postgres    false    207            d           1259    17205    galeriler_id_uindex    INDEX     N   CREATE UNIQUE INDEX galeriler_id_uindex ON public.galeriler USING btree (id);
 '   DROP INDEX public.galeriler_id_uindex;
       public            postgres    false    209            l           1259    17289    kayitlar_id_uindex    INDEX     L   CREATE UNIQUE INDEX kayitlar_id_uindex ON public.kayitlar USING btree (id);
 &   DROP INDEX public.kayitlar_id_uindex;
       public            postgres    false    215            V           1259    17151    yetki_id_uindex    INDEX     F   CREATE UNIQUE INDEX yetki_id_uindex ON public.yetki USING btree (id);
 #   DROP INDEX public.yetki_id_uindex;
       public            postgres    false    201            o           2606    17337 !   duyurular duyurular_gruplar_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.duyurular
    ADD CONSTRAINT duyurular_gruplar_id_fk FOREIGN KEY (grup_id) REFERENCES public.gruplar(id) ON UPDATE CASCADE ON DELETE CASCADE;
 K   ALTER TABLE ONLY public.duyurular DROP CONSTRAINT duyurular_gruplar_id_fk;
       public          postgres    false    213    203    2923            p           2606    17342 &   duyurular duyurular_kullanicilar_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.duyurular
    ADD CONSTRAINT duyurular_kullanicilar_id_fk FOREIGN KEY (kullanici_id) REFERENCES public.kullanicilar(id) ON UPDATE CASCADE ON DELETE CASCADE;
 P   ALTER TABLE ONLY public.duyurular DROP CONSTRAINT duyurular_kullanicilar_id_fk;
       public          postgres    false    2921    211    203            r           2606    17332 %   etkinlikler etkinlikler_gruplar_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.etkinlikler
    ADD CONSTRAINT etkinlikler_gruplar_id_fk FOREIGN KEY (grup_id) REFERENCES public.gruplar(id);
 O   ALTER TABLE ONLY public.etkinlikler DROP CONSTRAINT etkinlikler_gruplar_id_fk;
       public          postgres    false    205    2923    213            q           2606    17327 *   etkinlikler etkinlikler_kullanicilar_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.etkinlikler
    ADD CONSTRAINT etkinlikler_kullanicilar_id_fk FOREIGN KEY (kullanici_id) REFERENCES public.kullanicilar(id) ON UPDATE CASCADE ON DELETE CASCADE;
 T   ALTER TABLE ONLY public.etkinlikler DROP CONSTRAINT etkinlikler_kullanicilar_id_fk;
       public          postgres    false    205    2921    211            t           2606    17322    forumlar forumlar_gruplar_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.forumlar
    ADD CONSTRAINT forumlar_gruplar_id_fk FOREIGN KEY (grup_id) REFERENCES public.gruplar(id) ON UPDATE CASCADE ON DELETE CASCADE;
 I   ALTER TABLE ONLY public.forumlar DROP CONSTRAINT forumlar_gruplar_id_fk;
       public          postgres    false    207    2923    213            s           2606    17317 $   forumlar forumlar_kullanicilar_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.forumlar
    ADD CONSTRAINT forumlar_kullanicilar_id_fk FOREIGN KEY (kullanici_id) REFERENCES public.kullanicilar(id) ON UPDATE CASCADE ON DELETE CASCADE;
 N   ALTER TABLE ONLY public.forumlar DROP CONSTRAINT forumlar_kullanicilar_id_fk;
       public          postgres    false    207    2921    211            v           2606    17312 !   galeriler galeriler_gruplar_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.galeriler
    ADD CONSTRAINT galeriler_gruplar_id_fk FOREIGN KEY (grup_id) REFERENCES public.gruplar(id) ON UPDATE CASCADE ON DELETE CASCADE;
 K   ALTER TABLE ONLY public.galeriler DROP CONSTRAINT galeriler_gruplar_id_fk;
       public          postgres    false    213    209    2923            u           2606    17307 &   galeriler galeriler_kullanicilar_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.galeriler
    ADD CONSTRAINT galeriler_kullanicilar_id_fk FOREIGN KEY (kullanici_id) REFERENCES public.kullanicilar(id) ON UPDATE CASCADE ON DELETE CASCADE;
 P   ALTER TABLE ONLY public.galeriler DROP CONSTRAINT galeriler_kullanicilar_id_fk;
       public          postgres    false    209    2921    211            y           2606    17297    kayitlar kayitlar_gruplar_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.kayitlar
    ADD CONSTRAINT kayitlar_gruplar_id_fk FOREIGN KEY (grup_id) REFERENCES public.gruplar(id) ON UPDATE CASCADE ON DELETE CASCADE;
 I   ALTER TABLE ONLY public.kayitlar DROP CONSTRAINT kayitlar_gruplar_id_fk;
       public          postgres    false    2923    215    213            x           2606    17292 $   kayitlar kayitlar_kullanicilar_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.kayitlar
    ADD CONSTRAINT kayitlar_kullanicilar_id_fk FOREIGN KEY (kullanici_id) REFERENCES public.kullanicilar(id) ON UPDATE CASCADE ON DELETE CASCADE;
 N   ALTER TABLE ONLY public.kayitlar DROP CONSTRAINT kayitlar_kullanicilar_id_fk;
       public          postgres    false    2921    215    211            w           2606    17302 %   kullanicilar kullanicilar_yetki_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.kullanicilar
    ADD CONSTRAINT kullanicilar_yetki_id_fk FOREIGN KEY (yetki) REFERENCES public.yetki(id) ON UPDATE CASCADE ON DELETE CASCADE;
 O   ALTER TABLE ONLY public.kullanicilar DROP CONSTRAINT kullanicilar_yetki_id_fk;
       public          postgres    false    2904    201    211           